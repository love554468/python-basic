import os
import io 

# print(os.getcwd())
z = 'Mã HS, Toán , Lý, Hóa, Sinh, Văn, Anh, Sử, Địa'
s = 'abcdefghijklmnopqrstuvwxyz'
list_mon_hoc = Z.split(",")
list_ten = [x for x in s]
f = open("diem_chitiet.txt", mode='w',encoding='utf-8')
f.write(z)
for i in list_ten[3]:
    tn=''
    xh=''
    for i in range(4):
        tn+=str(rd1())
    f.write(stri)



f.close()

x = "\n" 

def rd1():
    return " " + str(round(random.uniform(1,10),1))
# random_diem = 
def rd2():
    return " " + str(random.randint(1,10)) 


def writefile(filename, list_ten):
    f = io.open(filename, mode='w', encoding = 'utf-8')
    
    for j in list_ten[:5]:
        f.write(j+x)
        for i in list_mon_hoc[:4]:
            # f.write(i+rd1()+rd2()+rd1()+rd2()+x)
            f.write(i+rd1()+rd1()+rd1()+rd1()+x)
        for i in list_mon_hoc[4:]:
            f.write(i+rd1()+rd2()+rd1()+rd2()+rd1()+x)
    f.close()