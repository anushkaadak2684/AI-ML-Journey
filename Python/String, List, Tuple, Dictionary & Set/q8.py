list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = set(list1).intersection(set(list2))

if len(common) == 0:
    print("No common elements exist")
else:
    print("Common elements exist")