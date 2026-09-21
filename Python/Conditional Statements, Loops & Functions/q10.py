def print_digits(n):
    while n > 0:
        print(n % 10)
        n = n // 10

n = int(input("Enter a number: "))
print_digits(n)