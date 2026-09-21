secret = 11
n = int(input("Guess the number: "))
if n > secret:
    print("Too high")
elif n < secret:
    print("Too low")
else:
    print("Correct!")