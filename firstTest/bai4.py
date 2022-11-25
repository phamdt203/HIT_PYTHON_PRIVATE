myList = list(map(str, input().split()))
myOutput1 = ''
for i in range(len(myList[0])):
    if (myList[0][i] != myList[0][i - 1] or i == 0):
        myOutput1 += str(myList[0].count(myList[0][i])) + str(myList[0][i])
myOutput2 = ''
for i in range (len(myOutput1)):
    if (myOutput1[i] != myOutput1[i - 1] or i == 0):
        myOutput2 += str(myOutput1.count(myOutput1[i],i, i+2)) + str(myOutput1[i])
print(myOutput1, myOutput2, sep='\n')