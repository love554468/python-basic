a,b = 1,0

try: 
    print(a/b)
except ZeroDivisionError:
    print("Chia cho so 0")
else:
    print("Neu khong co ngoai le xay ra")
finally:
    print("se luon luon chay lenh nay")