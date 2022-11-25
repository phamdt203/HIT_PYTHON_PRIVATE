n = int(input())
myList = sorted(list(map(int, input().split())), reverse=True)
myOutput = [str(i) for i in myList if sum([j for j in range(1,i) if i % j == 0]) > i]
print(len(myOutput), " ".join(myOutput), sep='\n')