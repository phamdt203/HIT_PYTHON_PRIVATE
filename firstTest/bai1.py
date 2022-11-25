a = input().split()
dem = 0
print(sum([dem + 1 for i in range(len(a[1])) if a[0] == a[1][i:i+len(a[0])]]))