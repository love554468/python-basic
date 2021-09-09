class Dan_ong():
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi
    def xin_chao(self):
        # print(hello " + self.ten)
        return self.ten

Binh = Dan_ong("Binh","21")
# Binh.hoc_tap = "binh thuong"
# Binh.loi_song = "khoa hoc"
# Binh.tuong_lai = "Tuoi sang"

# print("Trinh do hoc tap cua Binh: " + Binh.hoc_tap)
# print("tuong lai: " + Binh.tuong_lai)
# print("Loi song: " + Binh.loi_song)
# print(Binh.ten)
Binh.xin_chao()
print(Binh.xin_chao())