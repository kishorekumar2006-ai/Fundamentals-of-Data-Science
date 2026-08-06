import pandas as pd

df = pd.read_csv("House_Sales.csv")

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

clean = df[(df["Price"]>=lower) & (df["Price"]<=upper)]

print(clean)