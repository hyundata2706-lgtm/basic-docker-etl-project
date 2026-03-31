import pandas as pd
import random
from datetime import datetime, timedelta
import os

def get_data():
    rows = []

    for i in range(1000):
        row = {
            "id": i,
            "user_id": random.choice([None, random.randint(100, 200)]),
            "order_date": random.choice([
                datetime.now().strftime("%Y-%m-%d"),
                datetime.now().strftime("%Y/%m/%d"),
                "",
                "2024-13-01"
            ]),
            "amount": random.choice([
                random.uniform(10, 1000),
                -random.uniform(10, 100),
                "abc"
            ]),
            "status": random.choice(["completed", "pending", None])
        }
        rows.append(row)
    os.makedirs("data",exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv("data/order_dirty.csv", index=False)

    print("Generated 1000 rows dirty data")
