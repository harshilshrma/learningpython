# Example text data
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Preprocessing: Lowercasing and removing punctuation
processed_documents = [doc.lower().replace('.', '') for doc in documents]

# Counting word frequencies
word_freq = {}
for doc in processed_documents:
    words = doc.split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

# Print the word frequencies
print("Word Frequencies:")
for word, freq in word_freq.items():
    print(f"'{word}': {freq}")
