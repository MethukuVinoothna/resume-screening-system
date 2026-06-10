import pandas as pd

def recommend_jobs(resume_skills):

    jobs = pd.read_csv("jobs.csv")

    recommendations = []

    for _, row in jobs.iterrows():

        role = row["Role"]

        job_skills = set(
            skill.strip().lower()
            for skill in row["Skills"].split(",")
        )

        matches = len(
            job_skills.intersection(resume_skills)
        )

        recommendations.append(
            (role, matches)
        )

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return recommendations[:3]
