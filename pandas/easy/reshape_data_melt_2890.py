import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    melted = pd.melt(report, id_vars = ['product'], value_vars = ['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], 
                     var_name = 'quarter', value_name = 'sales')

    return melted

report = [
    {"product": "Umbrella", "quarter_1": 417, "quarter_2": 224, "quarter_3": 379, "quarter_4": 611},
    {"product": "SleepingBag", "quarter_1": 800, "quarter_2": 936, "quarter_3": 93, "quarter_4": 875}
]

df = pd.DataFrame(report)

df = meltTable(df)

print(df)