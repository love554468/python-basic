class Student:
    def __init__(self,ten,diem) -> None:
        self.t = ten 
        converse_diem = list(map(int,diem.split()))
        self.to, self.ly,self.ho = converse_diem
    def print_diemtk(self):
        dtk = round((self.to +self.ly + self.ho)/3,2)
        print("The average mark of %s is %s"%(self.ho,dtk))


name = input()
diem = input()
a = Student(name,diem)
a.print_diemtk()
