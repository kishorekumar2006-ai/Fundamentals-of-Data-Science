import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("House_Sales.csv")

Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR

clean = df[(df["Price"]>=lower) & (df["Price"]<=upper)]

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.hist(df["Price"])
plt.title("Before")

plt.subplot(1,2,2)
plt.hist(clean["Price"])
plt.title("After")

plt.show()

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.boxplot(df["Price"])
plt.title("Before")

plt.subplot(1,2,2)
plt.boxplot(clean["Price"])
plt.title("After")

plt.show()