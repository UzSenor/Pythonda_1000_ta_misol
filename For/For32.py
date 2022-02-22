# For32. n butun son berilgan. Quyidagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi dastur
# tuzing. A(0)=1 A(k)=(A(k-1)+1)/k k=1,2,3,4,...
n = int(input("N="))
A0=1
for k in range(1, n+1):
    Ak=(A0+1)/k
    A0=Ak
    print(Ak, end=" ")
