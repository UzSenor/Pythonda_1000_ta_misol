# For38. n butun sonlar berilgan. Quyidagini hisoblang. 1**n+2**(n-1)+...N**1
n = int(input("N="))
S=0
for i in range(1,n+1):
    S+=i**(n-i+1)
print(S)
