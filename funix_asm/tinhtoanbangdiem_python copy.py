import os
import io
# print(os.getcwd())

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

def conv(lst):
    lis = t,l,h,s,v,a,su,d = [float(i) for i in lst]
    # lis = [t,l,h,s,v,a,su,d]
    dtb_chuan = ((t + v + a) * 2.0 + (l + h + s + su + d) * 1.0) / 11.0
    ma_xl = ""
    if dtb_chuan > 9.0 and all([float(i)>8.0 for i in lis]):
        ma_xl = "Xuat sac"
    elif dtb_chuan > 8.0 and all([float(i)>6.5 for i in lis]):
        ma_xl = "Gioi"
    elif dtb_chuan > 6.5 and all([float(i)>5.0 for i in lis]):
        ma_xl = "Kha"
    elif dtb_chuan > 6.0 and all([float(i)>4.5 for i in lis]):
        ma_xl = "TB Kha"
    else:
        ma_xl = "TB"
    return ma_xl

def XL_KHTN(lst):
    xl = -1
    summ = sum([float(i) for i in lst])
    if summ >= 24:
        xl = 1
    elif 18 <= summ < 24:
        xl = 2
    elif 12<= summ < 18:
        xl = 3
    else:
        xl = 4 
    return xl

def XL_C(lst):
    xl = -1
    summ = sum([float(i) for i in lst])
    if summ >= 21:
        xl = 1
    elif 15 <= summ < 21:
        xl = 2
    elif 12<= summ < 15:
        xl = 3
    else:
        xl = 4 
    return xl

def XL_D(lst):
    xl = -1
    summ = sum([float(i) for i in lst ])
    if summ >= 32:
        xl = 1
    elif 24 <= summ < 32:
        xl = 2
    elif 20<= summ < 24:
        xl = 3
    else:
        xl = 4 
    return xl

class BANGDIEM:
    def load_dulieu(self,file_name):
        f = io.open(file_name,mode='r',encoding='utf-8')
        lines = f.readlines()
        lines = [i.replace("\n","") for i in lines]
        f.close()
        return lines
    def tinhdiem_trung_binh(self,fun):
        lines = fun
        d0 = lines[0].split(",")
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
        return dicc
    def luudiem_trungbinh(self,dic,file_name):
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

# a = BANGDIEM()
# a.luudiem_trungbinh(a.tinhdiem_trung_binh(a.load_dulieu(file_name)),fn_luudiem)

class DANHGIA(BANGDIEM):
    Khoi_A,Khoi_A1,Khoi_B,Khoi_C,Khoi_D = [],[],[],[],[]
    def load_dulieu(self, file_name):
        return super().load_dulieu(file_name)
    def xeploai_hocsinh(self,lines):
        dic = dict()
        for i in lines[1:]:
            i = i.replace("\n","").split(";")
            # print(i)
            dic[i[0]] = conv(i[1:])
        # print(dic)
        return dic

    def xeploai_thidaihoc_hocsinh(self,lines):
        list_lines = lines
        dicY = dict()
        for line in list_lines[1:]:
            inf_hs = line.split(";")
            DANHGIA.Khoi_A = inf_hs[1:4]
            DANHGIA.Khoi_A1 = [inf_hs[1],inf_hs[2],inf_hs[6]]
            DANHGIA.Khoi_B = [inf_hs[1],inf_hs[3],inf_hs[4]]
            DANHGIA.Khoi_C = [inf_hs[5],inf_hs[7],inf_hs[8]]
            DANHGIA.Khoi_D = [inf_hs[1],inf_hs[5],inf_hs[6],inf_hs[6]]
        #     listXL = [XL_KHTN(Khoi_A),XL_KHTN(Khoi_A1),XL_KHTN(Khoi_B),XL_C(Khoi_C),XL_D(Khoi_D)]
        #     dicY[inf_hs[0]] = listXL
        # return dicY
        # pass


class TUNHIEN(DANHGIA):
    def xeploai_hocsinh(self, lines):
        return [XL_KHTN(DANHGIA.Khoi_A),XL_KHTN(DANHGIA.Khoi_A1),XL_KHTN(DANHGIA.Khoi_B)]
            # listXL = [XL_KHTN(Khoi_A),XL_KHTN(Khoi_A1),XL_KHTN(Khoi_B),XL_C(Khoi_C),XL_D(Khoi_D)]
        #     dicY[inf_hs[0]] = listXL
        # return dicY    

class XAHOI(DANHGIA):
    def xeploai_hocsinh(self, lines):
        return [DANHGIA.XL_C(Khoi_C)]
class COBAN(DANHGIA):
    def xeploai_hocsinh(self, lines):
        return [DANHGIA.XL_D(Khoi_D)]
# a = DANHGIA()
# print(a.xeploai_hocsinh(a.load_dulieu(fn_luudiem)))
# print(a.xeploai_thidaihoc_hocsinh(a.load_dulieu(fn_luudiem)))

def main():
    # file_name = "F:/FOCUS/python/funix_asm/asm2/diem_chitiet.txt"
    file_name = "diem_chitiet.txt"
    fn_luudiem = "diem_trungbinh.txt"
    a = BANGDIEM()
    a.luudiem_trungbinh(a.tinhdiem_trung_binh(a.load_dulieu(file_name)),fn_luudiem)
    b = DANHGIA()
    dic1 = b.xeploai_hocsinh(b.load_dulieu(fn_luudiem))
    dic2 = b.xeploai_thidaihoc_hocsinh(b.load_dulieu(fn_luudiem))
    f = io.open("danhgia_hocsinh.txt",mode='w',encoding='utf-8')
    f.write('Ma HS  xeploai_TB chuan  xeploai_A  xeploai_A1  xeploai_B  xeploai_C  xeploai_D\n')
    for i in dic1:
        a = str(dic2[i])
        a = a.replace('[',"")
        a =a.replace(']',"")
        # print(i,dic1[i],a)
        s = i +";"+dic1[i]+";"+a+"\n"
        f.write(s)
    # “Nguyen Hai Nam; Gioi; 1; 1; 1; 3; 2”.
    f.close()


if __name__ == "__main__":
    main()
