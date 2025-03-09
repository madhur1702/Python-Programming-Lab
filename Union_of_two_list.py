import itertools
l1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    numbers1 = int(input('Enter any number: '))
    l1.append(numbers1)
l2 = []
num2 = int(input('Enter size of list 2: '))
for n in range(num2):
    numbers2 = int(input('Enter any number: '))
    l2.append(numbers2)
    
union = list(set(l1).union(set(l2)))
print('1. The Union of two lists is:', union)

union_plus = l1 + l2
print("2. Using + Operator:", union_plus)

joined_list = [*l1, *l2]
print("3. Using unpacking operator:", joined_list)

concatenated_chain = list(itertools.chain(l1, l2)) 
print("4. Using itertools.chain():", concatenated_chain)

l1.extend(l2)
print("5. Using extend():", l1)
