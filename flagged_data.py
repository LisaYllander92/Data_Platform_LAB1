from string import whitespace

import pandas as pd
from websockets.cli import print_during_input

df = pd.read_csv("products.csv", sep=";")

branching_df = df.copy()

missing_df["id"] = missing_df["id"].isna()
missing_df["name"] = missing_df["name"].isna()
missing_df["price"] = missing_df["price"].isna()
missing_df["currency"] = missing_df["currency"].isna()
missing_df["created_at"] = missing_df["created_at"].isna()


missing_id_condition = branching_df["id"].isna()
df_missing_ids = branching_df[missing_id_condition].copy()
df_missing_ids.to_csv("missing_ids.csv", index=False)

wrong_name_condition = (branching_df["name"].astype(str).str.strip() == "") & branching_df["name"].notna()
df_wrong_name = branching_df[wrong_name_condition].copy()
df_wrong_name.to_csv("invalid_names.csv", index=False)

wrong_price_condition = pd.to_numeric(branching_df["price"], errors='coerce').isna() & branching_df["price"].notna()
df_wrong_price = branching_df[wrong_price_condition].copy()
df_wrong_price.to_csv("invalid_prices.csv", index=False)

wrong_currency_condition = (branching_df["currency"].astype(str).str.strip().str.len() != 3) & branching_df["currency"].notna()
df_wrong_currency = branching_df[wrong_currency_condition].copy()
df_wrong_currency.to_csv("invalid_currency.csv", index=False)

wrong_date_condition = pd.to_datetime(branching_df["created_at"], errors='coerce').isna() & branching_df["created_at"].notna()
df_wrong_date = branching_df[wrong_date_condition].copy()
df_wrong_date.to_csv("invalid_dates.csv", index=False)


branching_df["is_rejected"] = (
    missing_id_condition |
    wrong_name_condition |
    wrong_price_condition |
    wrong_currency_condition |
    wrong_date_condition
)


