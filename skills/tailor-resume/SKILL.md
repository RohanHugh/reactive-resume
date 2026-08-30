---
name: tailor-resume
description: >
  Given a job posting URL, duplicate the template resume, customise the summary,
  skills, design colours, and cover letter to match the role, and create an
  application record. All changes are made directly in the PostgreSQL database.
  Automatically invokes the humanizer skill on the cover letter and summary.
---

# Tailor Resume for Job Application

When the user provides a job posting URL, automate the full workflow: duplicate
the template resume, analyse the job, customise everything, and create an
application record.

## Invocation

The user says something like:

- "Customise my resume for this job: [URL]"
- "Tailor my template for [URL]"
- "Apply to this role: [URL]"

## Workflow

### Step 1: Fetch the job posting

1. Fetch the job URL using the WebFetch or fetch_url tool
2. Extract:
   - **Job title**
   - **Company name**
   - **Location**
   - **Salary** (if listed)
   - **Closing date**
   - **Job duties / responsibilities** (bulleted list)
   - **Requirements / qualifications** (bulleted list)
   - **Company description** (if available)
   - **Contact / application method**
   - **Recruiter name** (if listed)
3. If the page is behind a cookie wall or paywall, search the internet for the
   same job title + company to find a cached version

### Step 2: Research the company brand

1. Search the internet for the company name + "brand colours" or "brand
   guidelines" or "logo"
2. Look for primary brand colour(s) in hex format (e.g. `#b60011`)
3. If no brand guidelines are found, look at the company's website CSS for
   colour variables or the dominant colour in their logo/favicon
4. Fall back to a professional neutral palette if no brand colours can be found:
   - Primary: `rgba(2, 146, 168)` (teal)
   - Text: `rgba(0, 0, 0, 1)`
   - Background: `rgba(255, 255, 255, 1)`

### Step 3: Duplicate the template resume

1. Query the database for the template resume:
   ```sql
   SELECT id, data::text FROM resume WHERE slug = 'rohan-hugh-template';
   ```
2. Generate a new UUID for the new resume
3. Set the new resume name to: `"Rohan Hugh - [Job Title] at [Company]"`
4. Set the slug to: `"rohan-hugh-[job-title]-[company]"` (lowercase, hyphenated)
5. Insert the new resume row with the copied data

### Step 4: Customise the summary

Rewrite the summary to be tailored to the specific role. Follow these rules:

- **Do not hallucinate** — only use facts from the user's existing resume data
  or the job posting itself
- **Lead with the most relevant qualification** for this specific role
- **Mention the company name and role** in the last sentence
- **Keep it to 3-4 sentences** max
- **Use natural, human-sounding language** (avoid AI vocabulary like
  "seamless", "dynamic", "proven track record", "passionate about")
- **If the role is technical** (developer, IT): emphasise technical skills and
  problem-solving
- **If the role is customer-facing** (support, service desk): emphasise
  communication and troubleshooting
- **If the role is analytical** (data, compliance): emphasise analytical skills
  and attention to detail

### Step 5: Customise the headline

Set a short, punchy headline that matches the role, e.g.:
- "AI Developer | Computer Science Graduate"
- "IT Support Professional | Computer Science Graduate"
- "Junior Developer | Python & AI Enthusiast"

### Step 6: Customise the skills section

The template resume has a broad pool of skills. Select and tailor them for
the specific role by analysing the job description:

**Available skills in the template:**
- Python / PyTorch / LLM APIs (OpenAI, Hugging Face) / Prompt Engineering /
  llama.cpp (Ollama) / Python ML Stack (NumPy, Pandas) / Java / Git & GitHub /
  Docker & WSL / Linux / Windows Server / Networking (TCP/IP, DNS, DHCP) /
  Microsoft 365 & Office Suite / Hardware Troubleshooting / Customer-Facing
  Support / VSCode & Dev Containers

**Rules for tailoring:**

1. **Analyse the job posting** for keywords and required skills
2. **Re-order skills** so the most relevant ones for the role appear first
3. **Remove irrelevant skills** — e.g. remove hardware troubleshooting for a
   developer role, remove AI skills for an admin role
4. **Keep transferable skills** — customer support and communication skills are
   relevant for almost any role
5. **Write honest proficiency text** that reflects the user's actual level:
   - For AI/ML roles: "Used for deep learning coursework and LLM research"
   - For IT support roles: "Used for system administration and troubleshooting"
   - For developer roles: "Used daily for development and scripting"
6. **Add relevant skills from the template pool** that match the job
   requirements — if the job asks for "machine learning" and the template has
   PyTorch, include it with appropriate proficiency text
7. **Never fabricate a skill** that is not in the template pool

### Step 7: Customise the design colours

Set the resume's primary colour to match the company brand:

```sql
'{metadata,design,colors,primary}'
→ 'rgba(R, G, B, 1)'  -- company brand colour
```

Convert hex to rgba. If the brand colour is very light (e.g. yellow, pastel),
use a darker shade of the same hue for readability.

### Step 8: Write the cover letter

Write a tailored cover letter following these rules:

- **Opening paragraph**: Reference the company by name, the role, and where
  the job was found. If the company has a notable mission, values, or recent
  work, mention it to show you did your research.
- **Second paragraph**: Map the user's most relevant experience directly to
  the job duties. Use specific examples from the user's resume.
- **Third paragraph**: Tie the user's education and technical skills to the
  role's requirements.
- **Fourth paragraph** (optional): Mention secondary experience that
  demonstrates transferable skills (eCommerce, freelance, etc.).
- **Closing paragraph**: Express enthusiasm and invite further discussion.
- **Sign off**: "Kind Regards, Rohan Hugh"

**Tone rules:**
- Natural, human-sounding
- No em dashes
- No AI vocabulary ("seamless", "dynamic", "passionate about", "thrive in")
- Specific, not generic
- Each paragraph should feel like it could only be written for THIS role at
  THIS company

### Step 9: Humanise the cover letter and summary

After writing the cover letter and summary, run the humanizer skill on them
to remove any remaining AI writing patterns:

1. Extract the cover letter content from the database
2. Run the humanizer skill's process on it (draft → audit → rewrite)
3. Extract the summary content
4. Run the humanizer skill's process on it
5. Update both in the database with the humanised versions

### Step 10: Create an application record

```sql
INSERT INTO application (
  id, user_id, company, role, location, salary, status, source,
  source_url, job_description, resume_id, applied_at, created_at, updated_at
) VALUES (
  gen_random_uuid()::text,
  '019f5870-2fc6-768e-a4d0-7ec8cdf70a7d',
  '[company name]',
  '[job title]',
  '[location]',
  '[salary]',
  'saved',
  '[source - e.g. gov.je, Jersey Evening Post]',
  '[job URL]',
  '[brief job description]',
  '[new resume ID]',
  NOW(), NOW(), NOW()
);
```

### Step 11: Report back

Tell the user:
1. What resume was created (name + slug)
2. What company brand colour was applied
3. What skills were selected, reordered, and what proficiency text was written
4. A preview of the cover letter (first paragraph)
5. That the humanizer was run on the cover letter and summary
6. The application record status
7. Any assumptions made or things the user should review

## Database reference

**User ID:** `019f5870-2fc6-768e-a4d0-7ec8cdf70a7d`
**Template resume ID:** `d945b8dd-ab0c-4263-b696-84c4b3ce1838`
**Template resume slug:** `rohan-hugh-template`

**Resume table columns:**

| Column | Type | Notes |
|---|---|---|
| id | text | UUID, use gen_random_uuid()::text |
| name | text | Display name, e.g. "Rohan Hugh - AI Developer at ESH Solutions" |
| slug | text | URL slug, e.g. "rohan-hugh-ai-developer-esh-solutions" |
| data | jsonb | Full resume JSON |
| user_id | text | Always the user ID above |
| created_at | timestamptz | NOW() |
| updated_at | timestamptz | NOW() |

**Application table columns:**

| Column | Type | Notes |
|---|---|---|
| id | text | UUID, use gen_random_uuid()::text |
| user_id | text | Always the user ID |
| company | text | Company name |
| role | text | Job title |
| location | text | Job location |
| salary | text | Salary if listed |
| status | text | 'saved' initially |
| source | text | Where the job was found |
| source_url | text | The job posting URL |
| job_description | text | Brief summary of the role |
| resume_id | text | The new resume's ID |
| applied_at | timestamptz | NOW() |
| created_at | timestamptz | NOW() |
| updated_at | timestamptz | NOW() |

## JSON paths for updates

When updating resume data via `jsonb_set`, use these paths:

| Content | JSON path |
|---|---|
| Headline | `{basics,headline}` |
| Location | `{basics,location}` |
| Summary content | `{summary,content}` |
| Skills items | `{sections,skills,items}` |
| Design primary colour | `{metadata,design,colors,primary}` |
| Cover letter content | `{customSections,1,items,0,content}` |
| Cover letter recipient | `{customSections,1,items,0,recipient}` |
| Experience item N desc | `{sections,experience,items,N,description}` |
| Education item N desc | `{sections,education,items,N,description}` |
