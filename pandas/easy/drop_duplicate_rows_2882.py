import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    dropped = customers.drop_duplicates("email")
    return dropped

customers = [
    {"customer_id": 1, "name": "Ella", "email": "emily@example.com"},
    {"customer_id": 2, "name": "David", "email": "michael@example.com"},
    {"customer_id": 3, "name": "Zachary", "email": "sarah@example.com"},
    {"customer_id": 4, "name": "Alice", "email": "john@example.com"},
    {"customer_id": 5, "name": "Finn", "email": "john@example.com"},
    {"customer_id": 6, "name": "Violet", "email": "alice@example.com"}
]

df = pd.DataFrame(customers)

df = dropDuplicateEmails(df)

print(df)