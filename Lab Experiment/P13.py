import re
from collections import Counter

with open("sample_text.txt", "r") as file:
    text = file.read().lower()

words = re.findall(r'\b\w+\b', text)
frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)