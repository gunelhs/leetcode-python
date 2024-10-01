import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees

salaries = [
    {"name": "Jack", "salary": 19666},
    {"name": "Piper", "salary": 74754},
    {"name": "Mia", "salary": 62509},
    {"name": "Ulysses", "salary": 54866}
]

df = pd.DataFrame(salaries)

df = modifySalaryColumn(df)

print(df)