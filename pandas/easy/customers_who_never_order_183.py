import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    joined = customers.merge(orders, left_on = "id", how = 'left', right_on = "customerId").get(["name", "customerId"])
    
    final = joined.query("customerId.isnull()").get(["name"]).rename(columns = {"name": "Customers"})

    return final

customers = pd.DataFrame(
[
    {'id': 1, 'name': 'Joe'},
    {'id': 2, 'name': 'Henry'},
    {'id': 3, 'name': 'Sam'},
    {'id': 4, 'name': 'Max'}
]
)

orders = pd.DataFrame(
    [    
    {'id': 1, 'customerId': 3},
    {'id': 2, 'customerId': 1}
]
)


df = find_customers(customers, orders)

print(df)