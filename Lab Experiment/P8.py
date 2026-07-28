import pandas as pd

df = pd.read_csv("Sales_data.csv")

top_5_products = df.groupby("Product")["Price"].sum().nlargest(5)

print("Five most sold products:")
print(top_5_products)