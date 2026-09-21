tup = tuple(map(int, input("Enter numbers: ").split()))
even_tup = ()
odd_tup = ()
for i in tup:
    if i % 2 == 0:
        even_tup += (i,)
    else:
        odd_tup += (i,)

print("Even tuple:", even_tup)
print("Odd tuple:", odd_tup)