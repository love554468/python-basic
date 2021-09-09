def inp():
    str = input("Nhap ten va tuoi theo cu phap(ten tuoi): ")
    str = str.split()
    print("Chao %s , ban se 100 tuoi vao nam %s"%(str[0],2021+100-int(str[1])))


if __name__ == "__main__":
    inp()