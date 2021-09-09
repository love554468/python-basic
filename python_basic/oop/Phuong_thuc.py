class NhanVien:
    def __init__(self,name,inf) -> None:
        self.name = name
        converse_inf = list(map(float,inf.split(", ")))
        self.thang,self.lcb,self.snlv,self.hsl = converse_inf
    def tinh_luong(self):
        tong_luong = self.lcb*self.snlv*self.hsl - 1000000
        return tong_luong*0.9 if tong_luong/1000000 > 9 else tong_luong
    def print_luong(self):
        luong = NhanVien.tinh_luong(self)
        print("Luong cua nhan vien %s nhan duoc trong thang %s la: %s VND."%(self.name,int(self.thang),luong))



name = input()
inf = input()
a = NhanVien(name,inf)
a.print_luong()
