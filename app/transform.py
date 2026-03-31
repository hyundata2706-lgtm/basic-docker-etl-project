import pandas as pd

def transform_data():
    df = pd.read_csv("data/order_dirty.csv")
    # drop null values
    df = df.dropna(subset=["user_id","order_date"])
    # change datatiem
    df["order_date"] = pd.to_datetime(df["order_date"],errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
    # remove invalid values
    df = df.dropna(subset=["user_id","order_date"])
    df = df[df["amount"] > 0]
    # busines logic
    df['status'] = df["status"].fillna('unknown')
    # drop duplicates
    df = df.drop_duplicates()
    
    print(df.isnull().sum())
    print(df.describe())
