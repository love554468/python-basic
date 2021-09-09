import re

stringg = '''nam thang 20, nguyen dinh binh
            nguyen van binh '''


reg = re.compile(r'nguyen(.*?)binh')

kq = reg.search(stringg)

print(kq.group(1))

regg =  re.compile(r'nguyen(.*?)binh')

kq2  = regg.findall(stringg)

print(kq2)

# def docc():
#     "van la doc nhung dung ngoac kep"
#     """ this 
#     is doc """
#     ''' this is
#     doc'''

# print(docc.__doc__);            
