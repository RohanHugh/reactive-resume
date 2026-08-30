import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import type { SemanticNode } from "@reactive-resume/resume/stylesheet";
import { describe, expect, it } from "vitest";
import { templateSchema } from "@reactive-resume/schema/templates";
import { buildAllTemplatesFixture } from "./all-templates-fixture";
import { resolveResumeRuntime } from "./resolve";
import { getResumeExportData } from "@reactive-resume/resume/export-sections";

const flattenKinds = (node: SemanticNode): string[] => [
	node.kind,
	...node.children.flatMap(flattenKinds),
];

const documentSource = readFileSync(fileURLToPath(new URL("../document.tsx", import.meta.url)), "utf8");

describe("cover-letter header via semantic runtime", () => {
	it("wires renderOptions (includeCoverLetterHeader) into the semantic runtime", () => {
		// Regression guard for the wiring in document.tsx: the semantic runtime must be built
		// from headerResumeData (which carries renderOptions), not the bare resumeData.
		expect(documentSource).toContain(
			"resolveResumeRuntime({ data: headerResumeData, template, mode: stylesheetMode })",
		);
	});

	it("renders a header node when includeCoverLetterHeader is enabled", () => {
		for (const template of templateSchema.options) {
			const full = buildAllTemplatesFixture(template);

			// Build a cover-letter-only document (the export path) that carries renderOptions,
			// mirroring how document.tsx passes headerResumeData into resolveResumeRuntime.
			const data = {
				...getResumeExportData(full, "cover-letter"),
				renderOptions: { includeCoverLetterHeader: true },
			} as never;

			const { sourceTree } = resolveResumeRuntime({
				data,
				template,
				source: undefined,
				mode: "semantic",
			});

			const kinds = flattenKinds(sourceTree);

			// Cover-letter-only + header toggle must yield a page-level header node.
			expect(kinds).toContain("header");
		}
	});

	it("omits the header node when includeCoverLetterHeader is disabled", () => {
		const template = "onyx" as const;
		const full = buildAllTemplatesFixture(template);
		const data = getResumeExportData(full, "cover-letter") as never;

		const { sourceTree } = resolveResumeRuntime({
			data,
			template,
			source: undefined,
			mode: "semantic",
		});

		expect(flattenKinds(sourceTree)).not.toContain("header");
	});
});
