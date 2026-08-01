import os
import json
import pandas as pd

from parser import parse_resume
from similarity import calculate_similarity
from llm import analyze_resume

# Read Job Description
with open("data/job_description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()

resume_folder = "resumes"
resume_files = os.listdir(resume_folder)

results = []

for resume in resume_files:     # Iterate through each resume file in the resumes folder

    print(f"\nProcessing: {resume}")
    resume_path = os.path.join(resume_folder, resume)

    resume_text = parse_resume(resume_path)
  
    similarity = calculate_similarity(
        resume_text,
        job_description
    )
    print(f"Similarity Score: {similarity}")

    analysis = analyze_resume(
        resume_text,
        job_description,
        similarity
    )

    results.append(
        {
            "Resume": resume,
            "Similarity Score": similarity,
            "Analysis": analysis
        }
    )

results.sort(                               # Sort the results based on the similarity score in descending order
    key=lambda x: x["Similarity Score"],
    reverse=True
)

print("\n===== Resume Rankings =====\n")

for index, candidate in enumerate(results, start=1):

    print("=" * 60)
    print(f"Rank: {index}")
    print(f"Resume: {candidate['Resume']}")
    print(f"Similarity Score: {candidate['Similarity Score']}")
    print("\nAnalysis:")
    print(candidate["Analysis"])
    print("=" * 60)
    print()

df = pd.DataFrame(results)

df.to_csv(
    "output/ranking.csv",
    index=False
)

with open(
    "output/ranking.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        results,
        file,
        indent=4
    )