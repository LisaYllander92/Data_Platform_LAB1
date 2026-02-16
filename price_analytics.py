import pandas as pd

df = pd.read_csv("products_cleaned.csv")

analytics = df.copy()

print(analytics["price"])

