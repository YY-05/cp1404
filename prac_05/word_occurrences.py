texts = input("Text: ")
words = texts.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
width = max(len(word) for word in word_counts)
sorted_words = sorted(word_counts.keys())
for word in sorted_words:
    print(f"{word:{width}} : {word_counts[word]}")
