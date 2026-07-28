import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sales_data.csv")

Month_sales = df.groupby("Month_sales")["Price"].sum()

plt.plot(Month_sales.index, Month_sales, marker="o")
plt.title("Monthly Sales Data")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=60)
plt.show()

