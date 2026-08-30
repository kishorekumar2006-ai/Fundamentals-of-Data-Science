import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("House_Sales.csv")

plt.hist(df["Price"], bins=10)
plt.title("Histogram of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

print("Mean :", df["Price"].mean())
print("Median :", df["Price"].median())

if df["Price"].mean() > df["Price"].median():
    print("Right Skewed Distribution")
elif df["Price"].mean() < df["Price"].median():
    print("Left Skewed Distribution")
else:
    print("Approximately Normal")