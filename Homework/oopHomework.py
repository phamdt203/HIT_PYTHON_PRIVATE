import numpy as np
class Matrix:
    def __init__(self, n, m):
        self.m = m
        self.n = n

    # Nhap ma tran cau 1
    def nhapcau1(self):
        return [list(map(int, input().split())) for i in range(self.n)]

    # Nhap ma tran cau 2
    def nhapcau2(self):
        return np.array([[int(i) for i in input() if i.isnumeric() == True] for j in range(self.n)]), np.array([[int(i) for i in input() if i.isnumeric() == True] for j in range(self.n)])
        
    # Cong hai ma tran
    def cong(self, firstMatrix, secondMatrix):
        myMatrix = np.array(firstMatrix) + np.array(secondMatrix)
        print(np.array(myMatrix).reshape(self.n, self.m))
    
    # Tru hai ma tran
    def tru(self, firstMatrix, secondMatrix):
        myMatrix = np.array(firstMatrix) - np.array(secondMatrix)
        print(np.array(myMatrix).reshape(self.n, self.m))

    # Nhan hai ma tran
    def nhan(self, firstMatrix, secondMatrix):
        myMatrix = np.array(firstMatrix) * np.array(secondMatrix)
        print(np.array(myMatrix).reshape(self.n, self.m))
    
    # Tich hai ma tran
    def tich(self, firstMatrix, secondMatrix):
        if (len(firstMatrix) == len(secondMatrix[0])):
            print(np.array(firstMatrix).dot(np.array(secondMatrix)), sep='\n')
        else:
            print("Khong the nhan hai ma tran nay")
    def xuat(self, lastMatrix):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string += str(lastMatrix[i][j])
                string += ' '
            string += '\n'
        return string

myCase = list(map(int, input().split()))
# Cau 1
# myMatrix = Matrix(myCase[0], myCase[1])
# firstMatrix = myMatrix.nhapcau1()
# secondMatrix = myMatrix.nhapcau1()
# Matrix.cong(myMatrix,firstMatrix=firstMatrix, secondMatrix=secondMatrix)
# Matrix.tru(myMatrix, firstMatrix=firstMatrix, secondMatrix=secondMatrix)
# Matrix.nhan(myMatrix, firstMatrix=firstMatrix, secondMatrix=secondMatrix)
# Matrix.tich(myMatrix, firstMatrix=firstMatrix, secondMatrix=secondMatrix)

# Cau 2
# yourMatrix = Matrix(myCase[0], myCase[1])
# complexMatrix = yourMatrix.nhapcau2()
# Matrix.cong(yourMatrix,firstMatrix=complexMatrix[0], secondMatrix=complexMatrix[1])
# Matrix.tru(yourMatrix, firstMatrix=complexMatrix[0], secondMatrix=complexMatrix[1])
# Matrix.nhan(yourMatrix, firstMatrix=complexMatrix[0], secondMatrix=complexMatrix[1])
# Matrix.tich(yourMatrix, firstMatrix=complexMatrix[0], secondMatrix=complexMatrix[1])

# Cau 3
# newMatrix = Matrix(myCase[0], myCase[1])
# print(newMatrix.xuat([[6,12,18],[6,12,18],[6,12,18]]))