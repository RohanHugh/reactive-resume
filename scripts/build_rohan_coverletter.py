#!/usr/bin/env python3
"""Build Reactive Resume data JSON for Rohan's HomeNet cover letter."""
import json, uuid

def gen():
    return str(uuid.uuid4())

recipient_html = (
    "<p><strong>Dwayne Murray</strong></p>"
    "<p>HomeNet</p>"
    "<p>27 Beresford Street</p>"
    "<p>St Helier</p>"
    "<p>Jersey JE2 4WL</p>"
)

content_paras = [
    ("<p>Dear Mr Murray,</p>"),
    ("<p>I am writing to apply for the Service Delivery Coordinator role at "
     "HomeNet. I heard about the position through the local community and was "
     "immediately interested. HomeNet has built a strong reputation in Jersey "
     "as an independent broadband provider that puts customers first, and that "
     "is the kind of company I want to work for.</p>"),
    ("<p>My experience at Jersey Gaming Hub gave me solid grounding in "
     "customer-facing technical support. I was the first person customers came "
     "to with technology problems, and I learned to listen carefully, explain "
     "things plainly, and make sure people left with their issues sorted. I "
     "helped customers set up products, navigate digital tools, and troubleshoot "
     "hardware and software problems, all while working in a busy shop. That "
     "role taught me to stay calm under pressure and keep the focus on the "
     "person in front of me.</p>"),
    ("<p>My Computer Science degree from the University of Sussex gave me a good "
     "understanding of how communications technology works, from networking "
     "basics to the digital tools that support day-to-day service delivery. I am "
     "comfortable discussing technology with both technical and non-technical "
     "people, and I pick up new systems quickly. My A-Level ICT qualification "
     "also means I know the Microsoft Office suite well and am used to "
     "keyboard-based work.</p>"),
    ("<p>Outside of formal roles, I run my own eCommerce operation, which "
     "involves regular customer communication, managing enquiries, resolving "
     "issues, and keeping accurate records. I also worked as a freelance video "
     "editor, managing multiple projects and deadlines while staying in close "
     "contact with clients. These experiences have sharpened my ability to work "
     "as part of a team and deliver reliable service.</p>"),
    ("<p>I would like to bring my customer service skills and technical "
     "confidence to HomeNet's team. I would welcome the chance to discuss how I "
     "could contribute to your service delivery.</p>"),
    ("<p>Kind Regards,</p>"),
    ("<p><strong>Rohan Hugh</strong></p>"),
]
content_html = "".join(content_paras)

data = {
  "basics": {
    "name": "Rohan Hugh",
    "headline": "Customer Service & Technology Professional | Computer Science Graduate",
    "email": "rohanhugh1@gmail.com",
    "phone": "+44 7403 918 197",
    "location": "Jersey",
    "website": {"url": "https://rohan.je", "label": "rohan.je"},
    "customFields": [],
  },
  "picture": {
    "url": "", "size": 80, "hidden": True, "rotation": 0, "aspectRatio": 1,
    "borderColor": "rgba(0, 0, 0, 0.5)", "borderWidth": 0,
    "shadowColor": "rgba(0, 0, 0, 0.5)", "shadowWidth": 0, "borderRadius": 0,
  },
  "summary": {
    "icon": "article", "title": "", "hidden": True, "columns": 1,
    "keepTogether": False, "startOnNewPage": False, "content": "",
  },
  "metadata": {
    "page": {
      "gapX": 4, "gapY": 6, "format": "a4", "locale": "en-US",
      "marginX": 14, "marginY": 12, "hideIcons": False,
      "hideSectionIcons": True, "hideLinkUnderline": False,
    },
    "notes": "",
    "design": {
      "level": {"icon": "star", "type": "circle"},
      "colors": {"text": "rgba(0, 0, 0, 1)", "primary": "rgba(220, 38, 38, 1)", "background": "rgba(255, 255, 255, 1)"},
    },
    "layout": {
      "pages": [{"main": ["cover-letter"], "sidebar": [], "fullWidth": False}],
      "sidebarWidth": 35,
    },
    "template": "onyx",
    "styleRules": [],
    "stylesheet": {"mode": "semantic", "source": {"text": "@version 1;\n", "languageVersion": 1}},
    "typography": {
      "body": {"fontSize": 12, "fontFamily": "IBM Plex Serif", "lineHeight": 1.6, "fontWeights": ["400", "500"]},
      "heading": {"fontSize": 16, "fontFamily": "IBM Plex Serif", "lineHeight": 1.6, "fontWeights": ["600"]},
    },
  },
  "sections": {
    "awards": {"icon": "trophy", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "skills": {"icon": "compass-tool", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "profiles": {"icon": "messenger-logo", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "projects": {"icon": "code-simple", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "education": {"icon": "graduation-cap", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "interests": {"icon": "football", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "languages": {"icon": "translate", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "volunteer": {"icon": "hand-heart", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "experience": {"icon": "briefcase", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "references": {"icon": "phone", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "publications": {"icon": "books", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "certifications": {"icon": "certificate", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
  },
  "customSections": [
    {
      "title": "Cover Letter",
      "icon": "envelope-simple",
      "columns": 1,
      "hidden": False,
      "keepTogether": False,
      "startOnNewPage": False,
      "id": gen(),
      "type": "cover-letter",
      "items": [
        {"id": gen(), "hidden": False, "recipient": recipient_html, "content": content_html}
      ],
    },
  ],
}

with open("scripts/resume-rohan-coverletter.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Wrote scripts/resume-rohan-coverletter.json")
print("bytes:", len(json.dumps(data)))