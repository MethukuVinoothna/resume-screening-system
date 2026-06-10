skills_db = [
    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "aws",
    "docker",
    "git",
    "github",
    "linux",
    "flask",
    "django",
    "express",
    "data structures",
    "c++",
    "Postman",
    "mysql",
    "node.js",
    "data science",
    "mongodb"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_db:

        if skill in text:

            found_skills.append(skill)

    return found_skills
