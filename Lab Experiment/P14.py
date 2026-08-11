import pandas as pd

df = pd.read_csv("customer_data.csv")

age_frequency = df["Age"].value_counts().sort_index()

print("Age Frequency Distribution:")
print(age_frequency)