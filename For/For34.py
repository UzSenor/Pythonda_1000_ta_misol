# For34. n butun son berilgan. Quyidagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi dastur
# tuzing. A(1)=1 A(2)=2 A(k)=(A(k-2)+2*A(k-1))/3 k=3,4,...
n = int(input("N="))
A1=1
A2=2
for k in range(3, n+1):
    Ak=(A1+2*A2)/3
    A1=A2
    A2=Ak
    print(Ak, end=" ")
