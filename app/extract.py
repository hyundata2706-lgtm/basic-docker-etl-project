import pandas as pd

def transform_data():
  df = pd.read_csv("data/order_dirty.csv")
  print(df.describe())
