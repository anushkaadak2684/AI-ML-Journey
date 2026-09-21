word = input("Enter a word: ")
count = 0
for ch in word:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1

print("Number of vowels:", count)