import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Weather_data.csv")

plt.plot(df["Month"], df["Temperature"], marker="o")
plt.title("Temperature")
plt.xticks(rotation=60)
plt.show()

plt.scatter(df["Month"], df["Rainfall"])
plt.title("Rainfall")
plt.xticks(rotation=60)
plt.show()