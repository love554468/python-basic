import re

str = "afas a the rain in Spain asd a the rain in Spain"

x = re.search("^the.*Spain$",str)
y = re.findall("^the.*Spain$",str)
print(y)