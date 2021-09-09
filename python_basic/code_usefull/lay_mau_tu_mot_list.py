import random

list1 =  ['hey','what','are','u','doing','now']

num_sam = 2

list_sam = random.sample(list1,num_sam)

print(list_sam)


num = 123456

# Sử dụng map
list_of_digits = list(map(int, str(num)))

print(list_of_digits)
# [1, 2, 3, 4, 5, 6]

# Sử dụng kỹ thuật list comprehension
list_of_digits = [int(x) for x in str(num)]

print(list_of_digits)
# [1, 2, 3, 4, 5, 6]
 