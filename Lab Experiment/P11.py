import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sales_data.csv")

monthly_sales = df.groupby("Month_sales")["Price"].sum()

plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Line Plot")
plt.xticks(rotation=60)
plt.show()

plt.scatter(monthly_sales.index, monthly_sales.values)
plt.title("Scatter Plot")
plt.xticks(rotation=60)
plt.show()

plt.bar(monthly_sales.index, monthly_sales.values)
plt.title("Bar Plot")
plt.xticks(rotation=60)
plt.show()