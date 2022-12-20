import math
n=int(input("n="))
X=int(input("X="))
s=0
for i in range(0,n):
    s=s+((-1)*math.pow(X,2*n+1))/(2*n+1)
print("s=",s)
