from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import json
import os

from .llm import call_ollama
from .prompts import *
from .resume_builder import assemble_resume
from .pdf_export import export_pdf

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store the latest resume text
latest_resume = {"text": ""}

@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")

@app.get("/api/data")
def get_data():
    """Get the current data from sample_input.json"""
    with open("data/sample_input.json", "r") as f:
        return json.load(f)

@app.get("/generate")
def generate_resume():
    """Generate resume from sample_input.json data"""
    # Load data from file
    with open("data/sample_input.json", "r") as f:
        data = json.load(f)

    summary = call_ollama(SUMMARY_PROMPT.format(**data))
    skills = call_ollama(SKILLS_PROMPT.format(**data))
    projects = call_ollama(PROJECTS_PROMPT.format(**data))
    experience = call_ollama(EXPERIENCE_PROMPT.format(**data))

    resume = assemble_resume(data, {
        "summary": summary,
        "skills": skills,
        "projects": projects,
        "experience": experience
    })

    # Save to PDF
    export_pdf(resume)
    
    # Store for later access
    latest_resume["text"] = resume

    return {
        "status": "success",
        "resume_text": resume,
        "data": data
    }

@app.get("/download-pdf")
def download_pdf():
    """Download the generated PDF"""
    if os.path.exists("resume.pdf"):
        return FileResponse(
            "resume.pdf", 
            media_type="application/pdf", 
            filename="resume.pdf",
            headers={"Content-Disposition": "attachment; filename=resume.pdf"}
        )
    return {"error": "PDF not found. Please generate resume first."}
