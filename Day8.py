import random
import math
import numpy as np
import pandas as pd
def generate_data(n):
    students = []
    for i in range(1, n + 1):
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        pi = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)
        students.append((i, marks, attendance, assignment, pi))
    return students
def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }
    for student in data:
        sid, marks, attendance, assignment, _ = student

        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)
        elif 40 <= marks <= 70:
            categories["Average"].append(sid)
        elif 71 <= marks <= 90:
            categories["Good"].append(sid)
        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)
        else:
            categories["Good"].append(sid)
    return categories
def analyze_data(df):
    marks = df["Marks"].values
    mean_marks = sum(marks) / len(marks)
    median_marks = np.median(marks)
    std_dev = np.std(marks)
    max_marks = max(marks)
    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0][1]
    min_val = min(marks)
    max_val = max(marks)
    norm = []
    for x in marks:
        norm.append((x - min_val) / (max_val - min_val))
    df["Normalized Marks"] = norm
    consistency = std_dev < 15
    attendance_risk = len(df[df["Attendance"] < 50]) > 3
    high_achievement = len(df[(df["Marks"] > 90) & (df["Attendance"] > 80)]) >= 2
    if consistency and not attendance_risk:
        insight = "Stable Academic System"
    elif high_achievement:
        insight = "Moderate Performance"
    else:
        insight = "Critical Attention Required"
    summary_tuple = (float(mean_marks), float(std_dev), int(max_marks))
    return df, summary_tuple, correlation, insight
n = 24110011615 % 10 #my roll number
student_data = generate_data(n)
df = pd.DataFrame(student_data, columns=[
    "Student ID", "Marks", "Attendance", "Assignment", "Performance Index"
])
unique_marks = set(df["Marks"])
categories = classify_students(student_data)
df, summary_tuple, correlation, insight = analyze_data(df)
print("\nStudent Data\n")
print(df)
print("\nUnique Marks\n")
print(unique_marks)
print("\nCategories\n")
for key, value in categories.items():
    print(key, ":", value)
print("\nStatistical Summary (Mean, Std Dev, Max)\n")
print(summary_tuple)
print("\nCorrelation (Marks vs Attendance)\n")
print(correlation)
print("\nFinal Insight\n")
print(insight)
