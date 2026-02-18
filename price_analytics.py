import pandas as pd

df = pd.read_csv("products_cleaned.csv")
analytics = df.copy()

"""---- Mean price ----"""
mean_price = analytics["price"].mean()
print(f"Mean price: {mean_price}")

"""---- Median price ----"""
median_price = analytics["price"].median()
print(f"Median price: {median_price}")

# Using the uncleaned file to get correct data
dirty_df = pd.read_csv("products.csv", sep=';')
products = dirty_df.copy()

"""---- Number of products ----"""
num_products = products["name"].count()
print(f"Total number of products: {num_products}")

"""---- Number of products with missing price ----"""
missing_price = pd.to_numeric(products["price"], errors='coerce').isnull().sum()
print(f"Missing price: {missing_price}")

analytic_data = {
    "mean_price": [mean_price],
    "median_price": [median_price],
    "num_products": [num_products],
    "missing_price": [missing_price]}

#Sace to csv-file
analytics_df = pd.DataFrame(analytic_data)
analytics_df.to_csv("analytics_summary.csv", index=False)


price_analysis_df = pd.read_csv("products_cleaned.csv")
price_analysis = price_analysis_df.copy()

"""---- Top 10 most expensive products ----"""
most_expensive_products = price_analysis.nlargest(10, "price").copy()
print("Most expensive products:")
print(most_expensive_products[["name", "price"]])

# Save most expensive products in csv-file
most_expensive_products.to_csv("top_expensive_products.csv", index=False)

""" ----Top 10 most deviant prices----"""
deviant_price_df = pd.read_csv("products.csv", sep=';')
deviant_price =deviant_price_df.copy()

deviant_price['price'] = pd.to_numeric(deviant_price['price'], errors='coerce')
most_expensive_price = deviant_price.nlargest(2, "price").copy()
print(most_expensive_price)

most_cheep_price = deviant_price.nsmallest(3, "price").copy()
print(most_cheep_price)

missing_prices = deviant_price[deviant_price["price"].isna()].copy()
print(missing_prices)

# Save top deviant prices in csv-file
most_expensive_price['category'] = "Top Expensive"
most_cheep_price['category'] = "Top Cheap"
missing_prices['category'] = "Missing/Text Price"

deviant_df = pd.concat([most_expensive_price, most_cheep_price, missing_prices])

deviant_df.to_csv("deviant_prices.csv", index=False)
