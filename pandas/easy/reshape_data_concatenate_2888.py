import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    conc = pd.concat([df1, df2])

    return conc

df1 = pd.DataFrame([    
    {"student_id": 1, "name": "Mason", "age": 8},
    {"student_id": 2, "name": "Ava", "age": 6},
    {"student_id": 3, "name": "Taylor", "age": 15},
    {"student_id": 4, "name": "Georgia", "age": 17}
])

df2 = pd.DataFrame([    
    {"student_id": 5, "name": "Leo", "age": 7},
    {"student_id": 6, "name": "Alex", "age": 7}
])


df = concatenateTables(df1, df2)

print(df)