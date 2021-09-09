import math

def  kiemtra_tamgiac(inpp):
    Ax, Ay, Bx, By, Cx, Cy = inpp 
    x = math.sqrt((Cx - Bx)*(Cx - Bx) + (Cy - By)*(Cy - By))
    y = math.sqrt((Cx - Ax)*(Cx - Ax) + (Cy - Ay)*(Cy - Ay))
    z = math.sqrt((Ax - Bx)*(Ax - Bx) + (Ay - By)*(Ay - By))

    if(x+y>z and x+z>y and y+z>x):
        # print("True")
        return True
    else:
        # print("False")
        return False

def goccanh_tamgiac(inpp):
    Ax, Ay, Bx, By, Cx, Cy = inpp 
    x = math.sqrt((Cx - Bx)*(Cx - Bx) + (Cy - By)*(Cy - By))
    y = math.sqrt((Cx - Ax)*(Cx - Ax) + (Cy - Ay)*(Cy - Ay))
    z = math.sqrt((Ax - Bx)*(Ax - Bx) + (Ay - By)*(Ay - By))
    a,b,c = x,y,z
    # print(a,b,c)
    g_a = math.acos((b*b + c*c - a*a) /(2*b*c))
    g_a = round(g_a*180/math.pi,2)
    g_b = math.acos((a*a + c*c - b*b) /(2*c*a))
    g_b = round(g_b*180/math.pi,2)
    g_c = math.acos((b*b + a*a - c*c) /(2*b*a))
    g_c = round(g_c*180/math.pi,2)
    # AB,BC,CA = z,x,y
    lst = [round(z,2),round(x,2),round(y,2),g_a,g_b,g_c]
    # print(lst)
    return lst

def xet_tamgiac(inpp):
    re1 = ''
    re3 = ''
    AB, BC, AC, g_A, g_B, g_C = goccanh_tamgiac(inpp)
# vuong, tu can
    if(g_A == 90 or g_B == 90 or g_C == 90):
        re1 = 'vuong'
        if(g_A == 90):
            re3 = 'A'
        elif(g_B == 90):
            re3 = 'B'
        else:
            re3 = 'C'
    elif(g_A > 90 or g_B > 90 or g_C > 90):
        re1 = 'tu'
        if(g_A > 90):
            re3 = 'A'
        elif(g_B > 90):
            re3 = 'B'
        else:
            re3 = 'C'
    else:
        # print('nhon')
        re1 = 'nhon'
    # thuong, can , deu
    re2 = ''
    if(AB==BC and BC==AC):
        # print("deu")
        re2 = "deu"
    elif(AB==BC or BC==AC or AB==AC):
        # print("can")
        re2 = 'can'
        if(AB==BC):
            re3 = 'B'
        elif(BC==AC):
            re3 = 'C'
        else:
            re3 = 'A'
    else:
        # print("binh thuong")
        re2 = 'binh thuong'

    if(re1=='vuong' and re2 == 'can'):
        
        print("ABC la tam giac vuong can tai dinh",re3)
    elif(re1 == 'deu'):
        print("ABC là tam giac deu")
    elif(re1=='tu' and re2=='can'):
        if(g_A == g_B):
            re3 = 'C'
        elif(g_A == g_C):
            re3 = 'B'
        elif(g_B == g_C):
            re3= 'A'
        print("ABC la tam giac tu va can tai dinh",re3)
    elif(re1=='nhon'and re2=='can'):
        if(g_A == g_B):
            re3 = 'C'
        elif(g_A == g_C):
            re3 = 'B'
        elif(g_B == g_C):
            re3= 'A'
        print('ABC là tam giac can tai dinh',re3)
    else:
            print("ABC la tam giac %s tai dinh %s va la tam giac %s"%(re1,re3,re2))

def dientich_tamgiac(i):
    AB, BC, AC, g_A, g_B, g_C = goccanh_tamgiac(i)
    a,b,c = BC,AC,AB
# print(AB, BC, AC, g_A, g_B, g_C)
    cv=a+b+c
    p=cv/2
    dt=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return round(dt,2)

def duongcao_tamgiac(inp):
    AB, BC, AC, g_A, g_B, g_C = goccanh_tamgiac(inp)
    a,b,c = BC,AC,AB 
    dt = dientich_tamgiac(inp)
    # print(dt)
    h_a = round(2*dt/a,2)
    h_b = round(2*dt/b,2)
    h_c = round(2*dt/c,2)
    return [h_a,h_b,h_c]

def trungtuyen_tamgiac(inp):
    AB, BC, AC, g_A, g_B, g_C = goccanh_tamgiac(inp)
    a,b,c = BC,AC,AB  
    tta = round(math.sqrt((2*(b*b+c*c)-a*a)/4)*2/3,2)
    ttb = round(math.sqrt((2*(a*a+c*c)-b*b)/4)*2/3,2)
    ttc = round(math.sqrt((2*(a*a+b*b)-c*c)/4)*2/3,2)
    # print(tta)
    # print(ttb)
    # print(ttc)
    return [tta,ttb,ttc]


def tam_tamgiac(inp):
    # [0,1,2,0,0,0]
    G1 = round(sum([v for i,v in enumerate(inp) if not i%2])/3,2)
    G2 = round(sum([v for i,v in enumerate(inp) if i%2])/3,2)
    H1 = 0
    H2 = 0
    return [G1,G2,H1,H2]


def  giaima_tamgiac(inp):
    if(kiemtra_tamgiac(inp)):
        print("A, B, C hop thanh mot tam giac")
    else:
        print("A, B, C khong hop thanh mot tam giac")    
        return
    AB, BC, AC, g_A, g_B, g_C = goccanh_tamgiac(inp)
    print("1. So do co ban cua tam giac:")
    print("Chieu dai canh AB:",AB)
    print("Chieu dai canh CA:",AC)
    print("Chieu dai canh BC:",BC) 
    print("Goc A: ",g_A)
    print("Goc B: ",g_B)
    print("Goc C: ",g_C)   
    xet_tamgiac(inp)
    print("2. Dien tich cua tam giac ABC: ",dientich_tamgiac(inp))
    ha,hb,hc = duongcao_tamgiac(inp)
    print("3. So do nang cao tam giac ABC:")
    print("Do dai duong cao tu dinh A: ",ha)
    print("Do dai duong cao tu dinh B: ",hb)
    print("Do dai duong cao tu dinh C: ",hc)
    tta, ttb, ttc = trungtuyen_tamgiac(inp)
    print("Khoang cach den trong tam tu dinh A: ",tta)
    print("Khoang cach den trong tam tu dinh B: ",ttb)
    print("Khoang cach den trong tam tu dinh C: ",ttc)
    g1, g2, h1, h2 = tam_tamgiac(inp)
    print('4. Toa do mot so diem dac biet cua tam giac ABC:')
    print("Toa do trong tam: [%s, %s]"%(g1,g2))
    print("Toa do truc tam: [%s, %s]"%(h1,h2))

def main():
    input_to_do = [0,1,2,0,0,0]
    giaima_tamgiac(input_to_do)

if __name__ == "__main__":
     main()