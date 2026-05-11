sentence = input("Enter a sentence: ")

words = sentence.lower().split()

word_count = {}
for word in words:
    word = word.strip(".,!?;:\"'")
    if word:
        word_count[word] = word_count.get(word, 0) + 1

print("\nWord frequencies:")
print(word_count)

print("\nDetailed breakdown:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  '{word}': {count}")