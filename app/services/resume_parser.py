import fitz  # PyMuPDF
import docx
import ollama
import json
import re

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()

def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")

def parse_resume_with_llm(raw_text: str) -> dict:
    prompt = f"""
You are a resume parsing expert. Extract information from the resume below and return ONLY a valid JSON object with no explanation, no markdown, no code blocks.

Resume:
{raw_text}

Return this exact JSON structure:
{{
    "contact": {{
        "name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": ""
    }},
    "summary": "",
    "skills": [],
    "experience": [
        {{
            "company": "",
            "role": "",
            "duration": "",
            "responsibilities": []
        }}
    ],
    "education": [
        {{
            "institution": "",
            "degree": "",
            "year": ""
        }}
    ],
    "certifications": [],
    "projects": [
        {{
            "name": "",
            "description": "",
            "technologies": []
        }}
    ]
}}
"""
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_output = response["message"]["content"]

    try:
        cleaned = re.sub(r"```json|```", "", raw_output).strip()
        parsed = json.loads(cleaned)
        return parsed
    except json.JSONDecodeError:
        return {
            "error": "Failed to parse resume",
            "raw_output": raw_output
        }

def parse_resume(file_path: str) -> dict:
    raw_text = extract_text(file_path)
    parsed = parse_resume_with_llm(raw_text)
    return parsed