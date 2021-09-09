import os
import io 


def tbtn(s):
    a = ['5', ' 10', ' 15', ' 70']
    re = list(map(int,s.split(",")))
    h = 0
    for i in range(4):
        h+=re[i]*int(a[i])
    return round(h/100,2)

def tbxh(s):
    a = ['5', ' 10', ' 10', ' 15', ' 60']
    re = list(map(int,s.split(",")))
    h = 0
    for i in range(5):
        h+=re[i]*int(a[i])
    return round(h/100,2)
# print(os.getcwd())


def tinhdiem_trungbinh(file_name):
    f = io.open(file_name,mode='r',encoding='utf-8')
    lines = f.readlines()
    # print(lines)
    d0 = lines[0].replace("\n","").split(",")
    dicc = dict()
    d = [i for i in range(100)]
    for i in range(1,len(lines)):
        d[i] = lines[i].replace("\n","").split(";")
        # print(d[i])
        dic = dict()
        for j in range(1,9):
            dic[d0[j].strip()] = tbtn(d[i][j])
            if j>4:
                dic[d0[j].strip()] = tbxh(d[i][j])
        dicc[d[i][0]] = dic
        # print(dic)
    # print(dicc)
    f.close()
    return dicc
def luudiem_trungbinh(dic,file_name):
    f = open(file_name, mode='w',encoding='utf-8')
    f.write("Mã HS, Toán , Lý, Hóa, Sinh, Văn, Anh, Sử, Địa\n")  
    for i in dic:
        s =""
        l = [i]
        for j in dic[i]:
            l.append(str(dic[i][j]))
        s = ";".join(l)
        f.write(s+'\n')
    f.close()  

# print()
# print(tbtn('1,1,1,1'))
# a = tinhdiem_trungbinh(file_name)

# 

def main():
    file_name = 'diem_chitiet.txt'
    fn = "diem_trungbinh.txt"
    a = tinhdiem_trungbinh(file_name)
    # print(a)
    luudiem_trungbinh(a,fn)


if __name__ == "__main__":
    main()