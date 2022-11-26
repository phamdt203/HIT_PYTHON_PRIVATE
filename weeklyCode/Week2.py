# Hàm print đầy đủ
# print(*object, sep = '', end = '\n', file=sys.stdout, flush=False)
print("Pham Dinh Tien", "Pham ", sep = '....', end=' Tien\n')
# Pham Dinh Tien....Pham  Tien
#


# Sử dụng format
a = int(input()) # 5
b = int(input()) # 6
print("{} + {} = {}".format(a,b,a + b)) # 5 + 6 = 11


# Sử dụng f-strings
x = int(input()) # 7
y = int(input()) # 8
print(f'{x} + {y} = {x + y}') # 7 + 8 = 15


# Toán tử 3 ngôi 
a = 1
result = a * 2 if a % 2 == 0 else a * 3
print(result) # 3

# Lệnh pass dùng để xây dựng một khối lệnh trống rỗng, khi lặp mà
# không cần thực hiện lệnh thì cho pass vào vòng lặp vẫn chạy được
# bình thường
for i in range(0,10):
    pass


# Hàm enumerate là một built-in function của Python tự sinh ra index
# theo iterable
a = ["eat", "sleep", "repeat"]
for idx, val in enumerate(a):
    print(idx, val)
# 0 eat
# 1 sleep
# 2 repeat


# Có thể kết hợp for, while với else
for var in range(1,3):
    print("Tien")
else:
    print("Pham")

var = 1
while var <= 2:
    print("Tien")
    var = var + 1
else:
    print("Pham")


    