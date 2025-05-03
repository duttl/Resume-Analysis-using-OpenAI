import os
from openai import OpenAI
from dotenv import load_dotenv
import logging

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def analyze_resume(resume_text, job_description):
    try:
        prompt = f"""
        You are an Applicant Tracking System (ATS).
        Analyze the resume below in context of the job description.

        Respond with:
        - A match score (0–10)
        - Key skill matches
        - Areas for improvement

        Job Description:
        {job_description}

        Resume:
        {resume_text}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        logging.error(f"OpenAI API error: {e}")
        return "Error analyzing resume. Please try again."
