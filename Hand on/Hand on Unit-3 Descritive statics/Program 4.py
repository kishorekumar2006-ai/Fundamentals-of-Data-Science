import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Employee.csv")

plt.boxplot(df["Salary"].dropna())

plt.title("Salary Box Plot")
plt.ylabel("Salary")
plt.show()