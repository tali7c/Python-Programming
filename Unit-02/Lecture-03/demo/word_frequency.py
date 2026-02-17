text = "data science uses data to make decisions"

words = text.lower().split()

unique_words = set(words)

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Words:", words)
print("Unique words:", unique_words)
print("Frequency:")
for word, count in freq.items():
    print(f"{word}: {count}")
