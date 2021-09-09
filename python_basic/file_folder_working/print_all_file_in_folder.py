import glob  
import re

str = []

path = 'F:\\DOC\*.txt'   
files=glob.glob(path)   
for file in files: 
    # print(file)
    a= file
    # b = re.sub("F:\\\DOC\\\","",a)
    str.append(b)

print(str)

# phục vụ cho quote generator web 