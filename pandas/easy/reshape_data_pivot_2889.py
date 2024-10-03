import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivot = pd.pivot_table(weather, values = 'temperature', index = ['month'], columns = ['city'])

    return pivot

weather = [
        {"city": "Jacksonville", "month": "January", "temperature": 13},
    {"city": "Jacksonville", "month": "February", "temperature": 23},
    {"city": "Jacksonville", "month": "March", "temperature": 38},
    {"city": "Jacksonville", "month": "April", "temperature": 5},
    {"city": "Jacksonville", "month": "May", "temperature": 34},
    {"city": "ElPaso", "month": "January", "temperature": 20},
    {"city": "ElPaso", "month": "February", "temperature": 6},
    {"city": "ElPaso", "month": "March", "temperature": 26},
    {"city": "ElPaso", "month": "April", "temperature": 2},
    {"city": "ElPaso", "month": "May", "temperature": 43}
]

df = pd.DataFrame(weather)

df = pivotTable(df)

print(df)