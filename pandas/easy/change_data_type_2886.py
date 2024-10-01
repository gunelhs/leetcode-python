import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    changed = students.astype({'grade': int})

    return changed

students = [
    {"student_id": 1, "name": "Ava", "age": 6, "grade": 73},
    {"student_id": 2, "name": "Kate", "age": 15, "grade": 87}
]

df = pd.DataFrame(students)

df = changeDatatype(df)

print(df)