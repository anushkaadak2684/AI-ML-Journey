info = {
    "Anushka": 99,
    "Mainak": 97,
    "Mayukh": 100,
    "Tanisha": 92,
    "Debojit": 89,
    "Aditya": 85
}

while True:
    choice = input("Enter your choice: (A, B, C, D or Q to quit): ")
    match choice:
        case 'A':
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
            info.update({name: marks})

        case 'B':
            name = input("Enter name whose marks need to be updated: ")
            marks = int(input("Enter new marks: "))
            info[name] = marks

        case 'C':
            name = input("Enter name to be searched: ")
            print(name, info.get(name))

        case 'D':
            print(info)

        case _:
            break