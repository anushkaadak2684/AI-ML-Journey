list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
list3 = list1 + list2
list3.sort()
print("Sorted merged list:", list3)
