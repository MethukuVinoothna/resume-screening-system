# ==========================================
# IMPORT LIBRARIES
# ==========================================

# Streamlit is used to build the web application
import streamlit as st

# Matplotlib is used for charts and visualizations
import matplotlib.pyplot as plt

# Import functions from project files
from utils import extract_text, match_score
from ats import ats_score
from skills import extract_skills
from recommender import recommend_jobs
from suggestions import get_suggestions


# ==========================================
# PAGE CONFIGURATION
# ==========================================

# Configure browser tab settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)


# ==========================================
# TITLE SECTION
# ==========================================

st.title(
    "🤖 AI Resume Screening & ATS Analyzer"
)

st.caption(
    "Analyze resumes, identify skill gaps, calculate ATS scores, and discover suitable career paths."
)


# ==========================================
# USER INPUT SECTION
# ==========================================

# Upload Resume PDF
resume_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

# Paste Job Description
job_description = st.text_area(
    "📝 Paste Job Description"
)

# Variable to store resume text
resume_text = ""


# ==========================================
# EXTRACT TEXT FROM PDF
# ==========================================

if resume_file:

    # Read text from uploaded PDF
    resume_text = extract_text(
        resume_file
    )

    # Show extracted text in expandable section
    with st.expander(
        "📄 View Extracted Resume Text"
    ):
        st.write(
            resume_text
        )


# ==========================================
# ANALYZE BUTTON
# ==========================================

if st.button(
    "🔍 Analyze Resume"
):

    # Check if resume is uploaded
    if resume_file:

        # ==========================================
        # MATCH SCORE
        # ==========================================

        # Compare resume with job description
        # Uses TF-IDF and Cosine Similarity
        score = match_score(
            resume_text,
            job_description
        )

        # ==========================================
        # ATS SCORE
        # ==========================================

        # Calculate ATS score
        ats = ats_score(
            resume_text
        )

        # ==========================================
        # SCORE CARDS
        # ==========================================

        col1, col2 = st.columns(
            2
        )

        with col1:

            st.metric(
                "Match Score",
                f"{score}%"
            )

        with col2:

            st.metric(
                "ATS Score",
                f"{ats}/100"
            )

        # Progress Bar
        st.progress(
            int(score)
        )

        st.markdown("---")

        st.header(
            "📊 Analysis Results"
        )

        # ==========================================
        # SKILL EXTRACTION
        # ==========================================

        # Skills extracted from resume
        resume_skills = set(
            extract_skills(
                resume_text
            )
        )

        # Skills extracted from Job Description
        jd_skills = set(
            extract_skills(
                job_description
            )
        )

        # Skills missing in resume
        missing_skills = (
            jd_skills -
            resume_skills
        )

        # ==========================================
        # RESUME SKILLS
        # ==========================================

        st.subheader(
            "🛠 Resume Skills"
        )

        st.code(
            ", ".join(
                resume_skills
            )
        )

        # ==========================================
        # JOB DESCRIPTION SKILLS
        # ==========================================

        st.subheader(
            "📋 Job Description Skills"
        )

        st.code(
            ", ".join(
                jd_skills
            )
        )

        # ==========================================
        # MISSING SKILLS
        # ==========================================

        st.subheader(
            "❌ Missing Skills"
        )

        if missing_skills:

            st.code(
                ", ".join(
                    missing_skills
                )
            )

        else:

            st.success(
                "No Missing Skills Found!"
            )

        # ==========================================
        # SKILL GAP CHART
        # ==========================================

        st.subheader(
            "📈 Skill Gap Analysis"
        )

        # Create 3 columns
        # Place chart in middle column
        col1, col2, col3 = st.columns(
            [1, 1, 1]
        )

        with col2:

            fig, ax = plt.subplots(
                figsize=(4,2.5)
            )

            ax.bar(
                ["Present", "Missing"],
                [
                    len(resume_skills),
                    len(missing_skills)
                ]
            )

            ax.set_title(
                "Skill Gap",
                fontsize=8
            )
            ax.tick_params(
                labelsize=6
            )
		
            ax.set_ylabel(
                "Count"
            )

            st.pyplot(
                fig
            )

        # ==========================================
        # JOB RECOMMENDATIONS
        # ==========================================

        recommended_jobs = recommend_jobs(
            resume_skills
        )

        st.subheader(
            "💼 Recommended Jobs"
        )

        for role, match in recommended_jobs:

            st.success(
                f"{role} | Skill Match: {match}"
            )

        # ==========================================
        # IMPROVEMENT SUGGESTIONS
        # ==========================================

        suggestions = get_suggestions(
            missing_skills
        )

        st.subheader(
            "🚀 Resume Improvement Suggestions"
        )

        if suggestions:

            for suggestion in suggestions:

                st.info(
                    suggestion
                )

        else:

            st.success(
                "Your resume already matches the job requirements well!"
            )

        # ==========================================
        # DOWNLOAD REPORT
        # ==========================================

        report = f"""
AI Resume Screening Report

Match Score: {score}%

ATS Score: {ats}/100

Resume Skills:
{list(resume_skills)}

Job Description Skills:
{list(jd_skills)}

Missing Skills:
{list(missing_skills)}

Recommended Jobs:
{recommended_jobs}
"""

        st.download_button(
            label="📄 Download Report",
            data=report,
            file_name="resume_report.txt",
            mime="text/plain"
        )

    else:

        st.error(
            "Please upload a resume first."
        )


# ==========================================
# FOOTER
# ==========================================

st.markdown(
    "---"
)

st.caption(
    "Built with Python, NLP, Scikit-Learn, Pandas, Matplotlib and Streamlit"
)


