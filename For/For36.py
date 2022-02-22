# For36. N va K butun sonlar berilgan. Quyidagini hisoblang. 1**K+2**K+...N**K
N = int(input("N="))
K = int(input("K="))
S=0
for i in range(1,N+1):
    S+=i**K
print(S)
