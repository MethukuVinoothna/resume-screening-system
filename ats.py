import re

def ats_score(resume_text):

    score = 0

    if re.search(r'\S+@\S+', resume_text):
        score += 20

    if "skills" in resume_text.lower():
        score += 20

    if "education" in resume_text.lower():
        score += 20

    if "project" in resume_text.lower():
        score += 20

    if len(resume_text.split()) > 100:
        score += 20

    return score
