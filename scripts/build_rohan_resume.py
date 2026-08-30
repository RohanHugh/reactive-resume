#!/usr/bin/env python3
"""Build Reactive Resume data JSON for Rohan Hugh and emit it to a file."""
import json, uuid

def gen(n=1):
    return [str(uuid.uuid4()) for _ in range(n)]

data = {
  "basics": {
    "name": "Rohan Hugh",
    "headline": "Customer Service & Technology Professional | Computer Science Graduate",
    "email": "rohanhugh1@gmail.com",
    "phone": "+44 7403 918 197",
    "location": "Jersey",
    "website": {"url": "https://rohan.je", "label": "rohan.je"},
    "customFields": [
      {"id": gen()[0], "icon": "globe", "text": "rohan-hugh", "link": ""}
    ],
  },
  "picture": {
    "url": "", "size": 80, "hidden": False, "rotation": 0, "aspectRatio": 1,
    "borderColor": "rgba(0, 0, 0, 0.5)", "borderWidth": 0,
    "shadowColor": "rgba(0, 0, 0, 0.5)", "shadowWidth": 0, "borderRadius": 0,
  },
  "summary": {
    "icon": "article", "title": "", "hidden": False, "columns": 1,
    "keepTogether": False, "startOnNewPage": False,
    "content": (
      "<p><strong>Computer Science graduate from the University of Sussex "
      "with a First-Class Honours degree.</strong> Experienced in "
      "customer-facing technical support, helping people solve problems with "
      "technology and digital tools in busy environments. Comfortable discussing "
      "technical concepts with non-technical users, with close attention to "
      "detail. Looking for a role that combines strong customer service skills "
      "with an interest in communications and technology.</p>"
    ),
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
      "pages": [{"main": ["profiles", "summary", "education", "experience", "projects", "volunteer", "references"], "sidebar": ["skills", "certifications", "awards", "languages", "interests", "publications"], "fullWidth": False}],
      "sidebarWidth": 35,
    },
    "template": "onyx",
    "styleRules": [],
    "stylesheet": {"mode": "semantic", "source": {"text": "@version 1;\n", "languageVersion": 1}},
    "typography": {
      "body": {"fontSize": 10, "fontFamily": "IBM Plex Serif", "lineHeight": 1.5, "fontWeights": ["400", "500"]},
      "heading": {"fontSize": 14, "fontFamily": "IBM Plex Serif", "lineHeight": 1.5, "fontWeights": ["600"]},
    },
  },
  "sections": {
    "awards": {"icon": "trophy", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "skills": {
      "icon": "compass-tool", "items": [
        {
          "id": gen()[0], "hidden": False, "icon": "headset", "iconColor": "",
          "name": "Customer-Facing Technical Support", "proficiency": "Advanced", "level": 4,
          "keywords": ["First-line Support", "Issue Diagnosis", "Customer Guidance"],
        },
        {
          "id": gen()[0], "hidden": False, "icon": "microsoft-excel-logo", "iconColor": "",
          "name": "Microsoft 365 & Office Suite", "proficiency": "Advanced", "level": 4,
          "keywords": ["Excel", "Word", "PowerPoint"],
        },
        {
          "id": gen()[0], "hidden": False, "icon": "network", "iconColor": "",
          "name": "Networking (TCP/IP, DNS, DHCP)", "proficiency": "Intermediate", "level": 3,
          "keywords": ["TCP/IP", "DNS", "DHCP"],
        },
        {
          "id": gen()[0], "hidden": False, "icon": "terminal-window", "iconColor": "",
          "name": "Linux", "proficiency": "Intermediate", "level": 3,
          "keywords": ["Development", "Personal Projects"],
        },
        {
          "id": gen()[0], "hidden": False, "icon": "cpu", "iconColor": "",
          "name": "Hardware Troubleshooting", "proficiency": "Advanced", "level": 4,
          "keywords": ["Fault Diagnosis", "Repair", "Reselling"],
        },
      ],
      "title": "", "hidden": False, "columns": 1, "keepTogether": False, "startOnNewPage": False,
    },
    "profiles": {
      "icon": "messenger-logo", "items": [
        {
          "id": gen()[0], "hidden": False, "icon": "link-simple", "iconColor": "",
          "network": "Website", "username": "rohan.je",
          "website": {"url": "https://rohan.je", "label": "rohan.je", "inlineLink": False},
        },
        {
          "id": gen()[0], "hidden": False, "icon": "video-camera", "iconColor": "",
          "network": "Editing Portfolio", "username": "rohaneditingportfolio",
          "website": {"url": "https://rohaneditingportfolio.carrd.co/", "label": "rohaneditingportfolio.carrd.co", "inlineLink": False},
        },
      ],
      "title": "", "hidden": False, "columns": 1, "keepTogether": False, "startOnNewPage": False,
    },
    "projects": {
      "icon": "code-simple", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False,
    },
    "education": {
      "icon": "graduation-cap", "items": [
        {
          "id": gen()[0], "hidden": False,
          "school": "University of Sussex", "degree": "BSc (Hons)", "area": "Computer Science",
          "grade": "1st Class Honours (1:1)", "location": "Brighton & Hove",
          "period": "2023 - 2026",
          "website": {"url": "", "label": "", "inlineLink": False},
          "description": "<p></p>",
        },
        {
          "id": gen()[0], "hidden": False,
          "school": "Hautlieu", "degree": "A-Levels", "area": "ICT, Computer Science & Media Studies",
          "grade": "A Level 3 Maths: A", "location": "St. Helier, Jersey",
          "period": "2021 - 2023",
          "website": {"url": "", "label": "", "inlineLink": False},
          "description": "<p>A-Levels in ICT (C), Computer Science (C) and Media Studies (C), plus Level 3 Maths (A).</p>",
        },
      ],
      "title": "", "hidden": False, "columns": 1, "keepTogether": False, "startOnNewPage": False,
    },
    "interests": {
      "icon": "football", "items": [
        {"id": gen()[0], "hidden": False, "icon": "airplane", "iconColor": "", "name": "FPV Drones", "keywords": []},
        {"id": gen()[0], "hidden": False, "icon": "racquet", "iconColor": "", "name": "Badminton", "keywords": []},
        {"id": gen()[0], "hidden": False, "icon": "cube", "iconColor": "", "name": "3D Printing", "keywords": []},
        {"id": gen()[0], "hidden": False, "icon": "robot", "iconColor": "", "name": "AI & Machine Learning", "keywords": []},
        {"id": gen()[0], "hidden": False, "icon": "barbell", "iconColor": "", "name": "Gym", "keywords": []},
      ],
      "title": "", "hidden": False, "columns": 1, "keepTogether": False, "startOnNewPage": False,
    },
    "languages": {"icon": "translate", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "volunteer": {"icon": "hand-heart", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "experience": {
      "icon": "briefcase", "items": [
        {
          "id": gen()[0], "hidden": False,
          "company": "Jersey Gaming Hub", "position": "General Assistant / Product Developer",
          "location": "St. Helier", "period": "Apr 2022 - Jan 2023",
          "website": {"url": "", "label": "", "inlineLink": False}, "roles": [],
          "description": (
            "<ul><li><p>Provided first-line technical support to customers, diagnosing and "
            "resolving hardware, software and network issues in a fast-paced retail environment.</p></li>"
            "<li><p>Helped customers navigate systems, set up products and troubleshoot "
            "applications so they could get on with what they needed to do.</p></li>"
            "<li><p>Built and maintained interactive product demonstrations, diagnosed "
            "technical faults and ran regular system checks to catch problems before they "
            "affected customers.</p></li></ul>"
          ),
        },
        {
          "id": gen()[0], "hidden": False,
          "company": "Freelance", "position": "Video Editor",
          "location": "", "period": "Jun 2023 - Dec 2024",
          "website": {"url": "https://rohaneditingportfolio.carrd.co/", "label": "Editing Portfolio", "inlineLink": False},
          "roles": [],
          "description": (
            "<ul><li><p>Worked with creators to help them generate over £10,000 in freelance "
            "revenue through video editing services.</p></li>"
            "<li><p>Edited long-form and short-form content that achieved more than 10 million "
            "combined views across digital platforms.</p></li>"
            "<li><p>Managed the full post-production workflow, including cutting, colour grading, "
            "audio cleanup, subtitles, visual effects and final delivery.</p></li></ul>"
          ),
        },
      ],
      "title": "", "hidden": False, "columns": 1, "keepTogether": False, "startOnNewPage": False,
    },
    "references": {"icon": "phone", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "publications": {"icon": "books", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
    "certifications": {"icon": "certificate", "items": [], "title": "", "hidden": True, "columns": 1, "keepTogether": False, "startOnNewPage": False},
  },
  "customSections": [],
}

with open("scripts/resume-rohan.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Wrote scripts/resume-rohan.json")
print("bytes:", len(json.dumps(data)))