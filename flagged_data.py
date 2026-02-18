import pandas as pd

df = pd.read_csv("products_cleaned.csv")

branching_df = df.copy()
print("=== DEBUGGING ===")
print("Total rows:", len(branching_df))
print("\nNegative prices:")
print(branching_df[branching_df["price"] < 0][["id", "name", "price"]])
print("\nMissing IDs:")
print(branching_df[branching_df["id"].isna()][["id", "name", "price"]])
print("=== END DEBUG ===\n")

branching_df["price"] = pd.to_numeric(branching_df["price"], errors='coerce')

# --- CONDITIONS ---
missing_id_condition = branching_df["id"].isna()
wrong_name_condition = (branching_df["name"].astype(str).str.strip() == "") & branching_df["name"].notna()
invalid_price_condition = branching_df["price"].isna()  # Efter to_numeric är ogiltiga redan NaN
wrong_price_condition = (
    (branching_df["price"] < 0) |
    (branching_df["price"] == 0) |
    (branching_df["price"] > 4000)
) & branching_df["price"].notna()

wrong_currency_condition = (branching_df["currency"].astype(str).str.strip().str.len() != 3) & branching_df["currency"].notna()
wrong_date_condition = pd.to_datetime(branching_df["created_at"], errors='coerce').isna() & branching_df["created_at"].notna()


print("Missing ID count:", missing_id_condition.sum())
print("Invalid price count:", invalid_price_condition.sum())
print("\nFirst 10 rows of price column:")
print(branching_df["price"].head(10))
print("\nFirst 10 rows of id column:")
print(branching_df["id"].head(10))

# --- AVVISA ---
branching_df["is_rejected"] = (
    missing_id_condition |
    invalid_price_condition
)

# --- FLAGGA ---
branching_df["is_flagged"] = (
    wrong_name_condition |
    wrong_price_condition |
    wrong_currency_condition |
    wrong_date_condition
)

# --- SPARA ---
rejected_df = branching_df[branching_df["is_rejected"] == True]
rejected_df.to_csv("rejected_values.csv", index=False)
flagged_df = branching_df[branching_df["is_flagged"] == True]
flagged_df.to_csv("flagged_values.csv", index=False)
branching_df.to_csv("products_flagged.csv", index=False)