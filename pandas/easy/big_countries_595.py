import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    result = (world.query("area >= 3000000 or population >= 25000000").get(["name", "population", "area"]))

    return result

world = [
    {'name': 'Afghanistan', 'continent': 'Asia', 'area': 652230, 'population': 25500100, 'gdp': 20343000000},
    {'name': 'Albania', 'continent': 'Europe', 'area': 28748, 'population': 2831741, 'gdp': 12960000000},
    {'name': 'Algeria', 'continent': 'Africa', 'area': 2381741, 'population': 37100000, 'gdp': 188681000000},
    {'name': 'Andorra', 'continent': 'Europe', 'area': 468, 'population': 78115, 'gdp': 3712000000},
    {'name': 'Angola', 'continent': 'Africa', 'area': 1246700, 'population': 20609294, 'gdp': 100990000000}
]

df = pd.DataFrame(world)

df = big_countries(df)

print(df)