# For37. n butun sonlar berilgan. Quyidagini hisoblang. 1**1+2**2+...N**n
n = int(input("N="))
S=0
for i in range(1,n+1):
    S+=i**i
print(S)
