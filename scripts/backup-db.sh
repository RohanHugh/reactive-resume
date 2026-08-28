#!/usr/bin/env bash
# backup-db.sh — Dump the Reactive Resume PostgreSQL database to a timestamped .sql file.
#
# Usage:
#   ./scripts/backup-db.sh [--keep N] [--dir PATH]
#
#   --keep N   Keep the N most recent backups, delete older ones (default: 14)
#   --dir PATH Where to write backups (default: <repo-root>/backups)
#
# The Postgres server runs inside the docker compose service 'postgres' (or the
# container named 'reactive_resume-postgres-1'). This script dumps through the
# container so no host Postgres tools are required.
#
# Example cron (every day at 03:00). See README note in this repo.
#   0 3 * * * /path/to/reactive-resume-main/scripts/backup-db.sh

set -euo pipefail

# --- Locate repo root (this script lives in <root>/scripts) ------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

# --- Parse args ---------------------------------------------------------------
KEEP=14
BACKUP_DIR="${REPO_ROOT}/backups"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --keep)   KEEP="$2"; shift 2 ;;
    --dir)    BACKUP_DIR="$2"; shift 2 ;;
    *) echo "Unknown option: $1" >&2; echo "Usage: $0 [--keep N] [--dir PATH]" >&2; exit 1 ;;
  esac
done

# --- Find the postgres container ---------------------------------------------
CONTAINER="$(docker ps --format '{{.Names}}' | grep -Ei 'reactive.*postgres|postgres' | head -1 || true)"
if [[ -z "${CONTAINER}" ]]; then
  echo "ERROR: no postgres container found. Is 'docker compose up -d postgres' running?" >&2
  exit 1
fi

# --- Sanity-check that Postgres is reachable in the container ----------------
if ! docker exec "${CONTAINER}" pg_isready -U postgres -d postgres >/dev/null 2>&1; then
  echo "ERROR: postgres in '${CONTAINER}' is not ready." >&2
  exit 1
fi

# --- Back up ------------------------------------------------------------------
mkdir -p "${BACKUP_DIR}"
STAMP="$(date +%Y%m%d_%H%M%S)"
OUT="${BACKUP_DIR}/reactive_resume_${STAMP}.sql"

echo "Dumping database 'postgres' from '${CONTAINER}' -> ${OUT}"
docker exec "${CONTAINER}" pg_dump -U postgres -d postgres --format=plain --no-owner --clean > "${OUT}"

# Verify the dump is non-empty and genuinely a SQL dump.
if [[ ! -s "${OUT}" ]] || ! grep -q "PostgreSQL database dump" "${OUT}"; then
  echo "ERROR: backup file '${OUT}' looks invalid or empty. Removing it." >&2
  rm -f "${OUT}"
  exit 1
fi

echo "OK: backed up to ${OUT} ($(du -h "${OUT}" | cut -f1))"

# --- Rotate old backups ---------------------------------------------------------
# shellcheck disable=SC2012
COUNT="$(ls -1 "${BACKUP_DIR}"/reactive_resume_*.sql 2>/dev/null | wc -l || true)"
if [[ "${COUNT}" -gt "${KEEP}" ]]; then
  # Remove the OLDEST files first (ls sorts alphabetically == chronologically by timestamp).
  ls -1 "${BACKUP_DIR}"/reactive_resume_*.sql | head -n "$((COUNT - KEEP))" | while read -r OLD; do
    echo "Pruning old backup: ${OLD}"
    rm -f "${OLD}"
  done
fi

echo "DONE. $(ls -1 "${BACKUP_DIR}"/reactive_resume_*.sql 2>/dev/null | wc -l) backup(s) in ${BACKUP_DIR}"