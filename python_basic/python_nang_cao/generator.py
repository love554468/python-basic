def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# Vòng lặp for đảo ngược chuỗi
# Viết bởi Quantrimang.com
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)
# start https://quantrimang.com/generator-trong-python-165274