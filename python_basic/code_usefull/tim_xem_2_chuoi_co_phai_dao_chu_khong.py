from typing import Counter


str1,str2,str3 = "abc","cba","adc"

cnt_1,cnt_2,cnt_3 = Counter(str2), Counter(str1), Counter(str3)

if cnt_1 == cnt_2:
    print("la dao chu")

if cnt_2 == cnt_3:
    print("la dao chu")

else:
    print("Khong la dao chu")