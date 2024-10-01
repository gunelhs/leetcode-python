import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.salary * 2
    return employees

employees = [
    {"name": "Piper", "salary": 4548},
    {"name": "Grace", "salary": 28150},
    {"name": "Georgia", "salary": 1103},
    {"name": "Willow", "salary": 6593},
    {"name": "Finn", "salary": 74576},
    {"name": "Thomas", "salary": 24433}
]

df = pd.DataFrame(employees)

df = createBonusColumn(df)

print(df)