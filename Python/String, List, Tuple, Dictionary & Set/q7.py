string = input("Enter a string: ")
count = 0
for i in string:
    if i == ' ':
        count += 1
print("Count of spaces in string:", count)