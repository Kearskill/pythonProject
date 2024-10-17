import numpy as np

#Q1 create numpy array of 2X2
myArr = np.array([[1,2],[3,4]])
print (myArr, "\n")

#Q2 create random numpy arr of size 3 X 4
myRandomArr = np.random.randint(1,30,size =(3,4))
print (myRandomArr, "\n")

#Q3 Create a numpy array of ones and a numpy array of zeroes
myOneArr = np.ones((2,2))
print (myOneArr)
myZeroArr = np.zeros((2,2))
print (myZeroArr, "\n")

#Q4 Create a random numpy array of size 6x3 and transpose it
myRandomArr1 = np.random.randint(1,30,size = (6,3))
print ("Random \n",myRandomArr1)
myTransposeArr1 = np.transpose(myRandomArr1)
print("Transposed \n",myTransposeArr1,"\n\n\n")
# print("No library \n\n\n")
# for i in range(len(myRandomArr1)):
#     for j in range(len(myRandomArr1[0])):
#         pass
#     pass

#Q5 Create two random numpy array of size n x p and p x m and then compute the dot product
n = int(input("Input n:"))
p = int(input("Input p:"))
myArrN = np.random.randint(1,30, size =(n,p))
myArrP = np.random.randint(1,30, size =(p,n))
print(myArrN,"\n")
print(myArrP,"\n\n")
print("The dot product \n")
myArrDotProduct = np.dot(myArrN,myArrP)
print(myArrDotProduct)