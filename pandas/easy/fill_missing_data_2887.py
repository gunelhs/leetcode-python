import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products[['quantity']] = products[['quantity']].fillna(value = 0)

    return products

products = [
    {"name": "Wristwatch", "quantity": None, "price": 135},
    {"name": "WirelessEarbuds", "quantity": None, "price": 821},
    {"name": "GolfClubs", "quantity": 779, "price": 9319},
    {"name": "Printer", "quantity": 849, "price": 3051}
]

df = pd.DataFrame(products)

df = fillMissingValues(df)

print(df)