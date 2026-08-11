import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

df = pd.read_csv("data.csv")

text = " ".join(df["feedback"].astype(str)).lower()
words = re.findall(r"\b\w+\b", text)

words = [word for word in words if word not in ENGLISH_STOP_WORDS]

frequency = Counter(words)

n = int(input("Enter number of top words: "))

top_words = frequency.most_common(n)

print("\nTop", n, "most frequent words:")
for word, count in top_words:
    print(word, ":", count)

words_list = [x[0] for x in top_words]
counts = [x[1] for x in top_words]

plt.bar(words_list, counts)
plt.title("Top Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()