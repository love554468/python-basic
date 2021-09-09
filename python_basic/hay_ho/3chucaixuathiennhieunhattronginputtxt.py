
import os

print(os.getcwd)
os.chdir(r"F:\\FOCUS\python\hay_ho")

def reFi(NaFi):
    f = open(NaFi,mode='r')
    lines = f.readlines()
    str=''
    for line in lines:
        line = line.replace("\n","")
        str+=line
    # str = "".join(lines)
    f.close()
    return str

def sol(NaFi):
    # s = input("Enter string: ")
    s = reFi(NaFi)
    # s = s.replace('\n',"")
    l = len(s)
    dic = dict()
    for i in s:
        dic[i]=0
    for i in s:
        dic[i] += 1
    print('Ki tu   PhanTram')
    dic2 = dict()
    for i in dic:
        scalee = round(dic[i]/l,2)*100
        s= "  %s\t%s"%(i,scalee)
        dic2[i] = scalee
        print(s+"%")
    # print(dic2)
    # sorted(dic2.values)
    print('============================')
    sorted_dict = {}
    sorted_keys = sorted(dic2,key= dic2.get)
    for w in sorted_keys:
        sorted_dict[w] = dic2[w]
    print(dic2)
    print(sorted_dict)
    a = list(sorted_dict)
    print(a)
    print('============================')
    print("3 chu cai xuat hien nhieu nhat")
    for i in range(3):
        print(a[-i-1])

sol('input.txt')
