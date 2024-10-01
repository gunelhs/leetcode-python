import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    missing = students.dropna(subset = "name")
    return missing

students = [
    {"student_id": 32, "name": "Piper", "age": 5},
    {"student_id": 217, "name": None, "age": 19},
    {"student_id": 779, "name": "Georgia", "age": 20},
    {"student_id": 849, "name": "Willow", "age": 14}
]

df = pd.DataFrame(students)

df = dropMissingData(df)

print(df)