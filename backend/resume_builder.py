def assemble_resume(data, sections):
    resume = f"""
{data['name']}
{data['role']}

SUMMARY
{sections['summary']}

SKILLS
{sections['skills']}

PROJECTS
{sections['projects']}

EXPERIENCE
{sections['experience']}

EDUCATION
{data['education']}
"""
    return resume.strip()
