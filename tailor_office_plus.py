import json
import uuid
import sys

# Load template
with open('C:/Users/user/template_resume_data.json', 'r') as f:
    data = json.load(f)

# --- Generate new IDs ---
new_resume_id = str(uuid.uuid4())
new_resume_name = "Rohan Hugh - Office Product Sales Representative & Technician at Office Plus"
new_resume_slug = "rohan-hugh-office-product-sales-representative-technician-office-plus"

# --- Update basics ---
data['basics']['headline'] = "Office Product Sales & Technician | Customer-Facing IT Support"

# --- Update summary ---
data['summary']['content'] = (
    "<p>Customer-facing support professional with hands-on experience in technical troubleshooting, "
    "product demonstrations, and helping people get the most out of their technology. "
    "Having worked in a busy retail environment where I diagnosed hardware and software issues, "
    "built interactive demos, and supported customers face-to-face every day, I am comfortable "
    "balancing sales and technical tasks. I also hold a First-Class Honours degree in Computer Science "
    "and have a strong grasp of IT fundamentals. I am excited about the opportunity to bring my "
    "technical and customer service skills to the Office Plus team in St Helier.</p>"
)

# --- Update skills ---
skills_items = [
    {
        "id": "skill-customer-facing",
        "icon": "chat-circle",
        "name": "Customer-Facing Support",
        "proficiency": "Provided first-line technical support, product demonstrations, and face-to-face assistance in a busy retail environment",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": ""
    },
    {
        "id": "skill-hardware",
        "icon": "toolbox",
        "name": "Hardware Troubleshooting",
        "proficiency": "Diagnosed hardware faults, performed system checks, and maintained equipment in a retail setting",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": ""
    },
    {
        "id": "skill-m365",
        "icon": "microsoft-logo",
        "name": "Microsoft 365 & Office Suite",
        "proficiency": "Proficient in Excel, Word, and PowerPoint; holds A-Level ICT qualification",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": ""
    },
    {
        "id": "skill-networking",
        "icon": "network",
        "name": "Networking (TCP/IP, DNS, DHCP)",
        "proficiency": "Provided first-line network troubleshooting and support for customer devices",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": ""
    },
    {
        "id": "skill-git",
        "icon": "git-branch",
        "name": "Git & GitHub",
        "proficiency": "Used for version control in software development and collaborative projects",
        "level": 0,
        "hidden": False,
        "keywords": [],
        "iconColor": ""
    }
]
data['sections']['skills']['items'] = skills_items

# --- Update design colours ---
data['metadata']['design']['colors']['primary'] = "rgba(20, 106, 181, 1)"

# Office Plus secondary colour: #1C4199 -> rgba(28, 65, 153, 1)
style_rules = [
    {
        "id": "style-section-type-summary-heading",
        "label": "Summary: Section heading",
        "slots": {"heading": {"color": "rgba(28, 65, 153, 1)"}},
        "target": {"scope": "sectionType", "sectionType": "summary"},
        "enabled": True
    },
    {
        "id": "style-section-type-experience-heading",
        "label": "Experience: Section heading",
        "slots": {"heading": {"color": "rgba(28, 65, 153, 1)"}},
        "target": {"scope": "sectionType", "sectionType": "experience"},
        "enabled": True
    },
    {
        "id": "style-section-type-education-heading",
        "label": "Education: Section heading",
        "slots": {"heading": {"color": "rgba(28, 65, 153, 1)"}},
        "target": {"scope": "sectionType", "sectionType": "education"},
        "enabled": True
    }
]
data['metadata']['styleRules'] = style_rules

# --- Update layout ---
# Page 1: main sections with sidebar for skills and interests
data['metadata']['layout']['pages'][0]['main'] = ["summary", "experience", "education"]
data['metadata']['layout']['pages'][0]['sidebar'] = ["skills", "interests"]

# Page 2: cover letter
data['metadata']['layout']['pages'][1] = {
    "main": ["019fb8ce-fdf5-7226-9c2b-fa9cdd416440"],
    "sidebar": [],
    "fullWidth": False
}

# --- Write cover letter ---
cover_letter_content = (
    "<p>I am writing to apply for the Office Product Sales Representative & Technician role at Office Plus. "
    "Having grown up in Jersey, I know Office Plus as the go-to local supplier for office products, furniture, "
    "and business equipment, and I would be keen to join a team that keeps local businesses running smoothly.</p>"
    "<p>In my previous role at Jersey Gaming Hub, I was the first person customers turned to when they had "
    "technical problems. I diagnosed hardware and software faults, helped people set up products, and ran "
    "regular equipment checks to catch issues before they affected anyone. That role also involved building "
    "interactive product demonstrations and working on the sales floor, so I am used to the mix of hands-on "
    "technical work and customer-facing sales that this role calls for. I am comfortable explaining technical "
    "things in plain language and making sure customers walk away happy with what they have bought.</p>"
    "<p>I hold a First-Class Honours degree in Computer Science from the University of Sussex, which has given "
    "me strong analytical and problem-solving skills. I work with Windows and Linux systems, networking basics, "
    "and the Microsoft Office suite, and I pick up new tools and systems quickly. The job description mentions "
    "that full training will be given, and I am someone who learns fast and is not afraid to ask questions "
    "until I get things right.</p>"
    "<p>Alongside my main roles, I run my own small eCommerce business selling collector cards and vintage "
    "computing equipment, which involves researching products, writing accurate listings, handling customer "
    "enquiries, and managing post-sale support. I also worked as a freelance video editor, managing multiple "
    "projects and deadlines. Both have taught me to be organised, communicate clearly, and take pride in "
    "doing a job properly.</p>"
    "<p>I would welcome the chance to discuss how my skills and experience could contribute to the Office Plus "
    "team. Thank you for considering my application.</p>"
    "<p>Kind Regards,<br>Rohan Hugh</p>"
)

cover_letter_recipient = (
    "<p>Mick</p>"
    "<p>Office Plus</p>"
    "<p>10 Commercial Street</p>"
    "<p>St Helier</p>"
    "<p>JE2 3RU</p>"
)

# Update the cover letter items
for section in data['customSections']:
    if section.get('type') == 'cover-letter' and section.get('id') == '019fb8ce-fdf5-7226-9c2b-fa9cdd416440':
        for item in section.get('items', []):
            item['content'] = cover_letter_content
            item['recipient'] = cover_letter_recipient
            break

# --- Hide the first (empty) cover letter section ---
for section in data['customSections']:
    if section.get('type') == 'cover-letter' and section.get('id') == '019fb8c8-7b3c-7376-9583-aa3d8171cc6d':
        section['hidden'] = True
        break

# --- Write the modified JSON to a file with proper encoding ---
with open('C:/Users/user/new_resume_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Output the new resume ID and other info
print(f"NEW_RESUME_ID={new_resume_id}")
print(f"NEW_RESUME_NAME={new_resume_name}")
print(f"NEW_RESUME_SLUG={new_resume_slug}")
print("DONE")