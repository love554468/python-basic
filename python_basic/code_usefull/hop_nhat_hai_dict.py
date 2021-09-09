from typing import Dict


dic1,dic2 = dict(),dict()

for i in range(4):
    dic1[i] = i+1
    dic2[i] = i+2

dic3 = {**dic1, ** dic2}

print(dic3)