# count most frequent words in a file

words = []
with open("text1.txt", "r") as f:
    for line in f:
        words.extend(line.split())

from collections import Counter
counts = Counter(words)
freq5 = counts.most_common(5)
print(freq5)


# count capital letters in a File

with open("text1.txt", "r") as f:
    count = 0
    count2 = 0
    text = f.read()
    for i in text:
        if i.isupper():
            count += 1
        if i.islower():
            count2 += 1
    print("upper: ", count)
    print("lower: ", count2)