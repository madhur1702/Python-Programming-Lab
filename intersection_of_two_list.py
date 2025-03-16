def intersection_list(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

n1 = int(input("Enter the number of elements in the first list: "))
list1 = []
for i in range(n1):
    element = int(input(f"Enter element {i+1}: "))
    list1.append(element)

n2 = int(input("Enter the number of elements in the second list: "))
list2 = []
for i in range(n2):
    element = int(input(f"Enter element {i+1}: "))
    list2.append(element)

intersection = intersection_list(list1, list2)

print("List 1 =", list1)
print("List 2 =", list2)
print("Intersection of two lists =", intersection) 
