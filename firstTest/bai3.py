n = int(input())
myList = list(map(int, input().split()))
print(len([k for k in [len([j for j in range(1, i + 1) if i % j == 0]) for i in myList] if len([g for g in range(2, k) if k % g == 0]) == 0 and k >= 2]) if len([k for k in [len([j for j in range(1, i + 1) if i % j == 0]) for i in myList] if len([g for g in range(2, k) if k % g == 0]) == 0 and k >= 2]) > 0 else "KHôNG")