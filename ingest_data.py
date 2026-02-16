import pandas as pd
from websockets.cli import print_during_input

df = pd.read_csv("products.csv", sep=";")

missing_df = pd.DataFrame

print(missing_df.isna())

missing_df["id"] = missing_df["id"].isna()
missing_df["name"] = missing_df["name"].isna()
missing_df["price"] = missing_df["price"].isna()
missing_df["currency"] = missing_df["currency"].isna()
missing_df["created_at"] = missing_df["created_at"].isna()

