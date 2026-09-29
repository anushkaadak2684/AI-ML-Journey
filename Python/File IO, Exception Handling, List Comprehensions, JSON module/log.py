with open("log.txt", "a") as f:
    f.write("\nProgram run successfully")

data = True
print("===All logs===\n")
with open("log.txt", "r") as f:
    while data:
        data = f.readline()
        print(data)
