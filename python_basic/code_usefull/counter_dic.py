# counter in python

from collections import Counter

stringg = ['a','b','c','d','a','e','c','c','c']

count_string = Counter(stringg)

print(count_string)


print(count_string['c'])

print(count_string.most_common(1))