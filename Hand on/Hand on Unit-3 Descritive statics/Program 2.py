import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Student_Marks.csv")

freq = df["Grade"].value_counts()

print(freq)

freq.plot(kind="bar")
plt.title("Frequency Distribution of Grades")
plt.xlabel("Grade")
plt.ylabel("Frequency")
plt.show()