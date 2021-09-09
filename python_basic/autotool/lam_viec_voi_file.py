import os
from shutil import copyfile
import io
#tao hoac mo mot file 
# f = open("binhnd.txt","w")
# f.close()

#doi ten file
# os.rename("binhnd.txt","binhnd1.txt")



# os.chdir(r"F:\STYLE\CODING\PYTHON")

# f = open("hellu.txt","w")
# # f.close()
# os.chdir(r"F:\STYLE\CODING\PYTHON")
# print(os.getcwd())


# remove file
# os.remove
# print(os.getcwd())

# os.remove("binhnd1.txt")

# os.chdir(r"F:\STYLE\CODING\PYTHON")

    # print(os.getcwd())

# os.remove("hellu.txt")

# tong ket lai thi da hoc tao file, getcwd, chdir, remove, rename

#khi làm việc với một file cần xem sét về đường dẫn thư mục đang thao tác
# đầu tiên lên kiểm tra đường dẫn, os.getcwd sau đó ta sẽ sửa đường dẫn bằng lệnh
#os.chdir()
os.chdir("F:\Data\MUZ")
print(os.getcwd())
# filename = "binhnd1.txt"
# writeline = "test hihi ddijt mệ cuộc đời này"

# def writefile(filename, writeline):
#     f = io.open(filename, mode='a', encoding = 'utf-8')
#     f.write(writeline + '\n')
#     f.close()

# # writefile(filename,writeline)

# def readfile(filename):
#     f = io.open(filename, mode="r", encoding='utf-8')
#     list_lines = f.readlines()
#     print(type(list_lines))
#     print(list_lines)
#     for line in list_lines:
#         print(line)

# readfile(filename)