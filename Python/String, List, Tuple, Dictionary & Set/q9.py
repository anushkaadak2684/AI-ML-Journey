numbers = list(map(int, input("Enter numbers: ").split()))
seen = set()
duplicates = set()

for i in numbers:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print("Duplicates elements:", duplicates)