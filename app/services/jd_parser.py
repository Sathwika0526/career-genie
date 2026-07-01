import ollama
import json
import re

def parse_jd_with_llm(jd_text: str) -> dict:
    """Send raw job description to Llama 3 and get structured data back."""

    prompt = f"""
You are a job description parsing expert. Extract information from the job description below and return ONLY a valid JSON object with no explanation, no markdown, no code blocks.

Job Description:
{jd_text}

Return this exact JSON structure with simple flat string arrays only:
{{
    "job_title": "",
    "company": "",
    "location": "",
    "role_type": "",
    "required_skills": ["skill1", "skill2"],
    "preferred_skills": ["skill1", "skill2"],
    "responsibilities": ["responsibility1", "responsibility2"],
    "tools_and_technologies": ["tool1", "tool2"],
    "experience_required": "",
    "education_required": "",
    "domain": ""
}}

Important: required_skills, preferred_skills, responsibilities and tools_and_technologies must be flat string arrays only. No nested objects.
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
            "error": "Failed to parse job description",
            "raw_output": raw_output
        }

def parse_jd(jd_text: str) -> dict:
    """Main function — takes raw JD text, returns structured data."""
    return parse_jd_with_llm(jd_text)