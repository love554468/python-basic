# import thư viện time
import time

# Kiểm tra thời gian bắt đầu
start_time = time.time()

# Code cần kiểm tra
a, b = 1, 2
c = a + b

# Kiểm tra thời gian kết thúc
end_time = time.time()

# Tính thời gian chênh lệch
time_taken_in_micro = (end_time - start_time)

# In kết quả
print (time_taken_in_micro)