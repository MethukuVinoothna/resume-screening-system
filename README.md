# AI Resume Screening System

## Overview

AI Resume Screening System is a Streamlit-based web application that analyzes resumes and evaluates their compatibility with job descriptions. The system calculates an ATS (Applicant Tracking System) score, extracts key skills, identifies missing skills, and provides personalized job recommendations.

## Features

* Resume PDF Upload
* ATS Score Calculation
* Resume Analysis
* Skill Extraction
* Missing Skills Identification
* Job Recommendations
* Interactive User Interface
* Real-time Results

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### Libraries Used

* Pandas
* NumPy
* Scikit-learn
* PyPDF2 / PDF Processing Libraries
* NLTK
* Regular Expressions (Regex)

## Project Workflow

1. Upload a resume in PDF format.
2. Extract text from the resume.
3. Analyze skills and keywords.
4. Compare resume content with job requirements.
5. Calculate ATS compatibility score.
6. Generate recommendations for improvement.
7. Suggest relevant job opportunities.

## Installation

Clone the repository:

```bash
git clone https://github.com/MethukuVinoothna/resume-screening-system.git
```

Navigate to the project directory:

```bash
cd resume-screening-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Project Structure

```text
resume-screening-system/
│
├── app.py
├── ats.py
├── skills.py
├── suggestions.py
├── recommender.py
├── utils.py
├── jobs.csv
├── requirements.txt
└── README.md
```

## Future Enhancements

* AI-powered resume feedback
* Resume ranking system
* Multiple job role support
* Advanced NLP-based skill matching
* Resume improvement suggestions using Generative AI
