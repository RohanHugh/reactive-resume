#!/usr/bin/env python3
"""Tailor resume for Junior Technician Support at Zenzero."""

import json
import psycopg2
import uuid
from datetime import datetime

# Database connection
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="postgres"
)
cur = conn.cursor()

# Get template resume
cur.execute("SELECT data FROM resume WHERE slug = 'rohan-hugh-template'")
template_data = cur.fetchone()[0]

# New resume details
new_id = str(uuid.uuid4())
resume_name = "Rohan Hugh - Junior Technician Support at Zenzero"
slug = "rohan-hugh-junior-technician-support-zenzero"
user_id = "019f5870-2fc6-768e-a4d0-7ec8cdf70a7d"

# Deep copy the template
data = json.loads(json.dumps(template_data))

# --- CUSTOMISE HEADLINE ---
data["basics"]["headline"] = "Junior IT Technician | Computer Science Graduate"

# --- CUSTOMISE SUMMARY ---
data["summary"]["content"] = (
    "<p>Computer Science graduate from the University of Sussex with a First-Class Honours degree "
    "and hands-on experience in technical support and troubleshooting. I spent nine months at Jersey "
    "Gaming Hub as the first point of contact for customer technical issues, diagnosing hardware, "
    "software, and network problems and getting them resolved quickly. I work with Windows, Linux, "
    "networking, and the Microsoft 365 suite, and I am comfortable picking up new systems and tools "
    "as I go. Looking for a Junior Technician Support role where I can apply my skills, learn from "
    "an experienced team, and grow within a company that values people and development.</p>"
)

# --- CUSTOMISE SKILLS ---
# For a Junior Technician Support role at Zenzero (IT support, Microsoft partner):
# Priority: Microsoft 365, Windows Server, Networking, Hardware Troubleshooting, Customer-Facing Support
data["sections"]["skills"]["items"] = [
    {
        "id": str(uuid.uuid4()),
        "icon": "microsoft-logo",
        "name": "Microsoft 365 & Office Suite",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": "",
        "proficiency": "Used daily for productivity, email, and collaboration support. Comfortable with Outlook, Teams, Word, Excel, and PowerPoint administration."
    },
    {
        "id": str(uuid.uuid4()),
        "icon": "monitor",
        "name": "Windows Server & Active Directory",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": "",
        "proficiency": "Experience with Windows environments through university coursework and personal projects. Familiar with user account management and group policy concepts."
    },
    {
        "id": str(uuid.uuid4()),
        "icon": "network",
        "name": "Networking (TCP/IP, DNS, DHCP)",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": "",
        "proficiency": "Studied networking fundamentals as part of Computer Science degree. Practical experience diagnosing connectivity issues in a retail support setting."
    },
    {
        "id": str(uuid.uuid4()),
        "icon": "wrench",
        "name": "Hardware Troubleshooting",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": "",
        "proficiency": "Diagnosed and resolved hardware faults at Jersey Gaming Hub. Built and tested computer systems, replaced components, and ran preventive maintenance checks."
    },
    {
        "id": str(uuid.uuid4()),
        "icon": "headset",
        "name": "Customer-Facing Support",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": "",
        "proficiency": "Provided first-line technical support to customers in a busy retail environment. Explained technical issues in plain language and followed up to make sure problems were resolved."
    }
]

# --- CUSTOMISE DESIGN COLOURS ---
# Zenzero brand: Orange primary (#E87722 or similar), dark grey for headings
# Converting to rgba: R=232, G=119, B=34 -> rgba(232, 119, 34, 1)
# Secondary (dark grey for section headings): rgba(51, 51, 51, 1)
data["metadata"]["design"]["colors"]["primary"] = "rgba(232, 119, 34, 1)"
data["metadata"]["design"]["colors"]["text"] = "rgba(0, 0, 0, 1)"
data["metadata"]["design"]["colors"]["background"] = "rgba(255, 255, 255, 1)"

# Section heading colours using dark grey
data["metadata"]["styleRules"] = [
    {
        "id": "style-section-type-summary-heading",
        "label": "Summary: Section heading",
        "slots": {"heading": {"color": "rgba(51, 51, 51, 1)"}},
        "target": {"scope": "sectionType", "sectionType": "summary"},
        "enabled": True
    },
    {
        "id": "style-section-type-experience-heading",
        "label": "Experience: Section heading",
        "slots": {"heading": {"color": "rgba(51, 51, 51, 1)"}},
        "target": {"scope": "sectionType", "sectionType": "experience"},
        "enabled": True
    },
    {
        "id": "style-section-type-education-heading",
        "label": "Education: Section heading",
        "slots": {"heading": {"color": "rgba(51, 51, 51, 1)"}},
        "target": {"scope": "sectionType", "sectionType": "education"},
        "enabled": True
    }
]

# --- CUSTOMISE LAYOUT ---
# Page 1: summary, experience, education in main; skills, interests in sidebar
data["metadata"]["layout"]["pages"][0]["main"] = ["summary", "experience", "education"]
data["metadata"]["layout"]["pages"][0]["sidebar"] = ["skills", "interests"]

# Page 2: Cover letter
data["metadata"]["layout"]["pages"][1] = {
    "main": ["019fb8ce-fdf5-7226-9c2b-fa9cdd416440"],
    "sidebar": [],
    "fullWidth": False
}

# --- HIDE EMPTY SECTIONS ---
for section_key in ["awards", "profiles", "projects", "volunteer", "references", "publications", "certifications", "languages"]:
    if section_key in data["sections"]:
        data["sections"][section_key]["hidden"] = True

# --- HIDE LEAST RELEVANT EXPERIENCE ---
# Hide the Freelance Video Editor (index 1) to fit on one page
data["sections"]["experience"]["items"][1]["hidden"] = True

# --- CUSTOMISE COVER LETTER ---
cover_letter_content = (
    "<p>Dear Hiring Manager,</p>"
    "<p>I am writing to apply for the Junior Technician Support role at Zenzero, as I have been following "
    "your work in the Jersey market and I am impressed by the range of services you provide, from managed "
    "IT support to cyber security and digital transformation. The chance to learn from an experienced team "
    "while working with real clients across regulated industries is exactly the kind of opportunity I am "
    "looking for.</p>"
    "<p>During my time at Jersey Gaming Hub, I was the first person customers came to with technical "
    "problems. I diagnosed hardware, software, and network issues, helped people set up products and "
    "troubleshoot applications, and ran regular equipment checks to catch problems before they affected "
    "customers. Handling multiple people at once in a busy shop taught me to stay calm, prioritise, and "
    "keep the focus on getting things working. I also built interactive product demonstrations and worked "
    "with the rest of the team to escalate anything I could not fix on my own.</p>"
    "<p>My Computer Science degree from the University of Sussex has given me a solid foundation in "
    "networking, operating systems, and problem-solving. I work with Windows, Linux, Python, and the "
    "Microsoft 365 suite, and I am comfortable picking up new tools and systems quickly. My A-Level "
    "ICT qualification also means I know the Microsoft Office suite well, which is useful when supporting "
    "users with day-to-day productivity software.</p>"
    "<p>Beyond my technical experience, I run my own eCommerce reselling operation, which involves "
    "customer communication, issue resolution, and keeping detailed records of every transaction. "
    "I also worked as a freelance video editor, managing multiple projects and deadlines while "
    "communicating clearly with clients, which taught me the kind of professionalism and reliability "
    "that matters in a support role.</p>"
    "<p>I am excited about the opportunity to join Zenzero and contribute to your Jersey team from day "
    "one. I am keen to develop my skills in a professional IT environment and grow alongside a company "
    "that clearly invests in its people. I would welcome the chance to discuss how my background and "
    "enthusiasm could benefit your team.</p>"
    "<p>Kind Regards,<br>Rohan Hugh</p>"
)

cover_letter_recipient = (
    "<p>Dear Hiring Manager</p>"
    "<p>Zenzero</p>"
    "<p>St Helier, Jersey</p>"
)

# Update the cover letter in customSections
for section in data["customSections"]:
    if section.get("id") == "019fb8ce-fdf5-7226-9c2b-fa9cdd416440":
        section["items"][0]["content"] = cover_letter_content
        section["items"][0]["recipient"] = cover_letter_recipient
        break

# --- INSERT NEW RESUME ---
now = datetime.utcnow()
cur.execute(
    """INSERT INTO resume (id, name, slug, data, user_id, created_at, updated_at)
       VALUES (%s, %s, %s, %s, %s, %s, %s)""",
    (new_id, resume_name, slug, json.dumps(data), user_id, now, now)
)

# --- CREATE APPLICATION RECORD ---
app_id = str(uuid.uuid4())
cur.execute(
    """INSERT INTO application (
        id, user_id, company, role, location, salary, status, source,
        source_url, job_description, resume_id, applied_at, created_at, updated_at
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
    (
        app_id,
        user_id,
        "Zenzero",
        "Junior Technician Support",
        "Jersey",
        "",  # Salary not listed
        "saved",
        "Jersey Evening Post",
        "https://jobs.jerseyeveningpost.com/jobs/junior-technician-support-jersey/60086-1/",
        "Junior Technician Support role providing first-line IT support, hardware troubleshooting, networking, and Microsoft 365 administration at Zenzero's Jersey office.",
        new_id,
        now, now, now
    )
)

conn.commit()

print(f"Resume created: {resume_name}")
print(f"Slug: {slug}")
print(f"Resume ID: {new_id}")
print(f"Application ID: {app_id}")
print(f"Primary colour: rgba(232, 119, 34, 1) (Zenzero orange)")
print(f"Section headings: rgba(51, 51, 51, 1) (dark grey)")
print("Skills: Microsoft 365, Windows Server, Networking, Hardware Troubleshooting, Customer-Facing Support")
print("Experience hidden: Freelance Video Editor (to fit on one page)")
print("Cover letter and summary written")

cur.close()
conn.close()
