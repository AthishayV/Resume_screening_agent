from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an expert HR Resume Screening Assistant.

Your task is to compare a candidate's resume with a job description.

You will receive:
1. A Job Description
2. A Resume
3. A Similarity Score (0-100)

Analyze the candidate and provide the following:

1. Candidate Summary
2. Extracted Skills
3. Experience Summary
4. Education
5. Matching Skills (skills present in both resume and JD)
6. Missing Skills (required by the JD but not found in the resume)
7. Recommendation (Shortlist / Consider / Reject)
8. Reason for your recommendation

Keep the response concise, professional, and easy to read.
"""

def analyze_resume(resume_text, job_description, similarity_score):     # Analyze a candidate's resume against a job description using the provided similarity score
        
    prompt = f"""
    Job Description:
    {job_description}
    
    --------------------------------------------------
    
    Resume:
    {resume_text}
    
    --------------------------------------------------
    
    Similarity Score:
    {similarity_score}
    
    Please analyze the resume based on the job description and provide:
    
    1. Candidate Summary
    2. Extracted Skills
    3. Experience Summary
    4. Education
    5. Matching Skills
    6. Missing Skills
    7. Recommendation
    8. Reason
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content