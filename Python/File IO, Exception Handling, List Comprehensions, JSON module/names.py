with open("names.txt", "w") as f:
    for i in range(6):
        name = input("Enter a name: ")
        f.write(name + "\n")

data = True
print("===Names===\n")
with open("names.txt", "r") as f:
    while data:
        data = f.readline()
        print(data)