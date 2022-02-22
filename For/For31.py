# For31. n butun son berilgan. Quyidagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi dastur
# tuzing. A(0)=2 A(k)=2+1/A(k-1) k=1,2,3,4,...
n = int(input("N="))
A0=2
for k in range(1, n+1):
    Ak=2+1/A0
    A0=Ak
    print(Ak, end=" ")
