words = ["apple", "banana", "kiwi", "cherry", "mango"]
dict = {}
for word in words:
    dict.update({word : len(word)})

print(dict)