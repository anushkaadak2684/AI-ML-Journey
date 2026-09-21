while True:
    n = input("Enter a number or Quit: ")
    if n == 'Quit':
        break
    elif int(n) > 0:
        print("Postive")
    elif int(n) < 0:
        print("Negative")
    else:
        print("Zero")