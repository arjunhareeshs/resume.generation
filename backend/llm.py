import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

def call_ollama(prompt, model=None):
    if model is None:
        model = os.getenv("MODEL_NAME", "mistral")
    
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt,
        text=True,
        capture_output=True,
        encoding='utf-8',
        errors='replace'
    )
    return result.stdout.strip()
