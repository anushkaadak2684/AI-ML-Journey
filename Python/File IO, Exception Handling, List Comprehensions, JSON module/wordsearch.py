data = True
l = 1
word = "Program"

with open("log.txt", "r") as f:
    while data:
        data = f.readline()
        if word in data:
            print(word, "found in line", l)
            break
        l += 1