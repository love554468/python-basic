import io

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

def xeploai_hocsinh(fn_inp):
    #trich suat tu file
    #xet cac dieu kien
    f = io.open(fn_inp,mode='r',encoding='utf-8')
    lines = f.readlines()
    # print(len(lines))
    # print(lines)
    dic = dict()
    for i in lines[1:]:
        i = i.replace("\n","").split(";")
        # print(i)
        dic[i[0]] = conv(i[1:])
    f.close()
    # print(dic)
    return dic

def xeploai_thidaihoc_hocsinh(file_name):
    f = io.open(file_name,mode = 'r',encoding='utf-8')
    list_lines = f.readlines() 
    dicY = dict()
    for line in list_lines[1:]:
        # print(line.replace("\t"," "))
        line = line.replace("\n","")
        # thong tin diem chi tiet cua hoc sinh - inf_hs theo list
        inf_hs = line.split(";")
        # print(inf_hs)
        # T L H S VA AN SU DI 
        # 1 2 3 4 5  6  7  8 
        Khoi_A = inf_hs[1:4]
        Khoi_A1 = [inf_hs[1],inf_hs[2],inf_hs[6]]
        Khoi_B = [inf_hs[1],inf_hs[3],inf_hs[4]]
        Khoi_C = [inf_hs[5],inf_hs[7],inf_hs[8]]
        Khoi_D = [inf_hs[1],inf_hs[5],inf_hs[6],inf_hs[6]]
        listXL = [XL_KHTN(Khoi_A),XL_KHTN(Khoi_A1),XL_KHTN(Khoi_B),XL_C(Khoi_C),XL_D(Khoi_D)]
        # print(listXL)
        dicY[inf_hs[0]] = listXL
    # print(dicY)
    return dicY



# print(xeploai_hocsinh(fn_inp))
# print(xeploai_thidaihoc_hocsinh(fn_inp))

def main(fn_input):
    dic1 = xeploai_hocsinh(fn_input)
    dic2 = xeploai_thidaihoc_hocsinh(fn_input)
    f = io.open("danhgia_hocsinh.txt",mode='w',encoding='utf-8')
    f.write('Ma HS  xeploai_TB chuan  xeploai_A  xeploai_A1  xeploai_B  xeploai_C  xeploai_D\n')
    for i in dic1:
        a = str(dic2[i])
        a = a.replace('[',"")
        a =a.replace(']',"")
# [str()] -> ",".join()
        # print(i,dic1[i],a)
        s = i +";"+dic1[i]+";"+a+"\n"
        f.write(s)
    # “Nguyen Hai Nam; Gioi; 1; 1; 1; 3; 2”.
    f.close()

if __name__ == "__main__":
    fn_input = "diem_trungbinh.txt"
    main(fn_input)
