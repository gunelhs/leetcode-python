import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:


    column_names = ['student_id', 'age']
    final_dataframe = pd.DataFrame(student_data, columns = column_names)
    return final_dataframe

print(createDataframe([[1,15],[2,11],[3,11],[4,20]]))