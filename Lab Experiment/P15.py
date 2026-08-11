import pandas as pd

df = pd.read_csv("likes_data.csv")

likes_frequency = df["Likes"].value_counts().sort_index()

print("Likes Frequency Distribution:")
print(likes_frequency)