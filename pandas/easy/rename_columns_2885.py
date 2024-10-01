import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns = {'id': 'student_id', 
    'first': 'first_name',
    'last': 'last_name',
    'age': 'age_in_years'}, inplace = True)

    return students

students = [
    {"id": 1, "first": "Mason", "last": "King", "age": 6},
    {"id": 2, "first": "Ava", "last": "Wright", "age": 7},
    {"id": 3, "first": "Taylor", "last": "Hall", "age": 16},
    {"id": 4, "first": "Georgia", "last": "Thompson", "age": 18},
    {"id": 5, "first": "Thomas", "last": "Moore", "age": 10}
]

df = pd.DataFrame(students)

df = renameColumns(df)

print(df)