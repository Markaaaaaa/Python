def word_frequency(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Input and Output
sentence = input("Enter a sentence: ")
frequencies = word_frequency(sentence)
print("Word frequencies:")
for word, count in frequencies.items():
    print(f"{word}: {count}")
