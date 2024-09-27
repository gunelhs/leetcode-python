import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:

    filtered = students.loc[students['student_id'] == 101, ['name', 'age']]

    return filtered

students = [
    {"student_id": 101, "name": "Ulysses", "age": 13},
    {"student_id": 53, "name": "William", "age": 10},
    {"student_id": 128, "name": "Henry", "age": 6},
    {"student_id": 3, "name": "Henry", "age": 11}
]

df = pd.DataFrame(students)

print(selectData(df))