# doc gia tri tai 1 o
# thay doi gia tri tai 1 o
from os import getcwd
import openpyxl
def get_value_sheet_in_wb(filename, cellname):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    wb.close()
    return Sheet1[cellname].value

filename = 'file.xlsx'
cellname = 'G6'
# a = get_value_sheet_in_wb(filename,cellname)
# print(a)

def update_value_sheet_in_wb(filename, cellname, value):
    wb = openpyxl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    Sheet1[cellname].value = value
    wb.close()
    wb.save(filename)

# update_value_sheet_in_wb(filename,cellname,value='binhdaptraivl')

username = 'A'
passwd = 'B'
#A10->A19
# for i in range(10,20):
#     user_name = "%s%s"%(username,i)
#     pass_word = "%s%s"%(passwd,i)
#     update_value_sheet_in_wb(filename,user_name,'binhnd' + str(i))
#     update_value_sheet_in_wb(filename, pass_word, '123' + str(i))


for i in range(10,20):
    user_name = "%s%s"%(username,i)
    pass_word = "%s%s"%(passwd,i)
    u = get_value_sheet_in_wb(filename,user_name )
    p = get_value_sheet_in_wb(filename,pass_word )
    print(u)
    print(p)
    input('enter to next!')


