SUMMARY_PROMPT = """
You are a professional resume writer.

Write a 3–4 line ATS-optimized professional summary.

Candidate:
Education: {education}
Skills: {skills}
Projects: {projects}
Target Role: {target_role}

Rules:
- Professional tone
- No fluff
- No headings
"""

SKILLS_PROMPT = """
Create an ATS-friendly SKILLS section.

Rules:
- Categorize skills
- Use bullet points
- Keep concise

Skills: {skills}
"""

PROJECTS_PROMPT = """
Write 2 project descriptions for a resume.

Projects:
{projects}

Rules:
- 3 bullets per project
- Start with action verbs
- ATS-friendly
"""

EXPERIENCE_PROMPT = """
Write resume experience bullets.

Experience:
{experience}

Rules:
- 3 bullets
- Use metrics where possible
- Professional tone
"""
