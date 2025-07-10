import re
from PyPDF2 import PdfReader

def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def split_text(text, max_len=800):
    paragraphs = text.split("\n")
    chunks = []
    chunk = ""
    for para in paragraphs:
        if len(chunk) + len(para) <= max_len:
            chunk += " " + para
        else:
            chunks.append(chunk.strip())
            chunk = para
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def extract_email(text):
    match = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return match[0] if match else "📭 Email not found."

def extract_phone(text):
    match = re.findall(r"\+?\d[\d\s\-]{8,15}", text)
    return match[0] if match else "📞 Mobile number not found."

def extract_skills(text):
    common_skills = [
        "AWS", "EC2", "S3", "RDS", "Lambda", "Docker", "Terraform", "Linux", "Python",
        "Java", "JavaScript", "React", "Next.js", "Git", "GitHub", "Scikit-learn",
        "Tailwind", "Flask", "Streamlit", "Firebase", "Kubernetes"
    ]
    found = [skill for skill in common_skills if skill.lower() in text.lower()]
    return "✅ Skills found: " + ", ".join(found) if found else "No skills found."

def extract_section(text, keyword):
    pattern = rf"{keyword}(.+?)(?=\n[A-Z][a-z]|$)"
    match = re.findall(pattern, text, re.IGNORECASE | re.DOTALL)
    return match[0].strip() if match else f"{keyword} not found."

def smart_answer(query, text):
    query_lower = query.lower()

    if "email" in query_lower:
        return extract_email(text)
    elif "phone" in query_lower or "mobile" in query_lower:
        return extract_phone(text)
    elif "skill" in query_lower:
        return extract_skills(text)
    elif "project" in query_lower:
        return extract_section(text, "Project")
    elif "experience" in query_lower:
        return extract_section(text, "Experience")
    elif "education" in query_lower:
        return extract_section(text, "Education")
    elif "github" in query_lower:
        return extract_section(text, "Github")
    elif "portfolio" in query_lower:
        return extract_section(text, "Portfolio")
    else:
        return None  # fallback to QA model
