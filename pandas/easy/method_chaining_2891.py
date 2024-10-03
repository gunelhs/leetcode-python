import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    heavyAnimals = (animals.query("weight >= 100").sort_values(by = "weight", ascending = False).get(["name"]))

    return heavyAnimals

animals = [
    {"name": "Tatiana", "species": "Snake", "age": 98, "weight": 464},
    {"name": "Khaled", "species": "Giraffe", "age": 50, "weight": 41},
    {"name": "Alex", "species": "Leopard", "age": 6, "weight": 328},
    {"name": "Jonathan", "species": "Monkey", "age": 45, "weight": 463},
    {"name": "Stefan", "species": "Bear", "age": 100, "weight": 50},
    {"name": "Tommy", "species": "Panda", "age": 26, "weight": 349}
]

df = pd.DataFrame(animals)

df = findHeavyAnimals(df)

print(df)