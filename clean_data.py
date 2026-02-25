import pandas as pd

df = pd.read_csv("products.csv", sep=";")
cleaning_data = df.copy()

""" ----Cleaning 'id'---- """

# Remove duplicates
cleaning_data = cleaning_data.drop_duplicates(subset=["id"])
cleaning_data["id"] = cleaning_data["id"].astype("string")
cleaning_data["id"] = cleaning_data["id"].str.strip()
cleaning_data["id"] = cleaning_data["id"].str.upper()
cleaning_data["id"] = cleaning_data["id"].str.replace(" ", "").str.replace("_", "-")
print(cleaning_data["id"])

""" ----Cleaning 'name'---- """
cleaning_data["name"] = cleaning_data["name"].astype("string")
cleaning_data["name"] = cleaning_data["name"].str.strip()
cleaning_data["name"] = cleaning_data["name"].str.title()
cleaning_data["name"] = cleaning_data["name"].str.replace(r"\s+", " ", regex = True)
print(cleaning_data["name"])

""" ----Cleaning 'price'---- """
# errors='coerce' transforms "not_available" or "free" to NaN automatically
cleaning_data["price"] = pd.to_numeric(cleaning_data["price"], errors='coerce')
print(cleaning_data["price"])

""" ----Cleaning 'currency'---- """
cleaning_data["currency"] = cleaning_data["currency"].str.strip()
cleaning_data["currency"] = cleaning_data["currency"].str.upper()
print(cleaning_data["currency"])

""" ----Cleaning 'created at'---- """
# Only allowing valid format on date (YYYY-MM-DD)
cleaning_data["created_at"] = cleaning_data["created_at"].astype("string")
cleaning_data['created_at'] = pd.to_datetime(cleaning_data['created_at'], errors='coerce', yearfirst=True)
print(cleaning_data["created_at"])


# Create new csv-file with cleaned data
cleaning_data.to_csv("products_cleaned.csv", index=False)
