# For35. n butun son berilgan. Quyidagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi dastur
# tuzing. A(1)=1 A(2)=2 A(3)=3 A(k)=A(k-1)+A(k-2)-2*A(k-3) k=4,...
n = int(input("N="))
A1=1
A2=2
A3=3
for k in range(4, n+1):
    Ak=A3+A2-2*A1
    A1=Ak
    A2=Ak+1
    A3=Ak+2
    print(Ak, end=" ")
