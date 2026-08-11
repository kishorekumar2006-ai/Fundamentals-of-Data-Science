import pandas as pd
import re
from collections import Counter

df = pd.read_csv("customer_reviews.csv")

text = " ".join(df["Review"].astype(str)).lower()
words = re.findall(r"\b\w+\b", text)

frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.most_common():
    print(word, ":", count)