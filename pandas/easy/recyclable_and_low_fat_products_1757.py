import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowFat_recyc = (products.query("low_fats == 'Y' and recyclable == 'Y'").get(["product_id"]))

    return lowFat_recyc

products = [
    {'product_id': 0, 'low_fats': 'Y', 'recyclable': 'N'},
    {'product_id': 1, 'low_fats': 'Y', 'recyclable': 'Y'},
    {'product_id': 2, 'low_fats': 'N', 'recyclable': 'Y'},
    {'product_id': 3, 'low_fats': 'Y', 'recyclable': 'Y'},
    {'product_id': 4, 'low_fats': 'N', 'recyclable': 'N'}
]

df = pd.DataFrame(products)

df = find_products(df)

print(df)