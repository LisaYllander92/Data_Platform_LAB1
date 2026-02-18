import pandas as pd

df = pd.read_csv("products_cleaned.csv")

analytics = df.copy()

print(analytics["price"])

# Mean price
mean_price = analytics["price"].mean()
print(f"Mean price: {mean_price}")

# Median price
median_price = analytics["price"].median()
print(f"Median price: {median_price}")

# Using the uncleaned file to get correct data
dirty_df = pd.read_csv("products.csv", sep=';')
products = dirty_df.copy()

# Number of products
num_products = products["name"].count()
print(f"Total number of products: {num_products}")

# Number of products with missing price
missing_price = pd.to_numeric(products["price"], errors='coerce').isnull().sum()
print(f"Missing price: {missing_price}")

analytic_data = {
    "mean_price": [mean_price],
    "median_price": [median_price],
    "num_products": [num_products],
    "missing_price": [missing_price]}

analytics_df = pd.DataFrame(analytic_data)
analytics_df.to_csv("analytics_summary.csv", index=False)



price_analysis_df = pd.read_csv("products_cleaned.csv")
price_analysis = price_analysis_df.copy()

# Top 10 most expensive products
most_expensive_products = price_analysis.nlargest(10, "price")
print("Most expensive products:")
print(most_expensive_products[["name", "price"]])
