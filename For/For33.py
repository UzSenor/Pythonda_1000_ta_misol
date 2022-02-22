# For33. n butun son berilgan. Quyidagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi dastur
# tuzing. F(1)=1, F(2)=1 F(k)=F(k-2)+F(k-1) k=3,4,...
n = int(input("N="))
F1=1
F2=1
for k in range(3, n+1):
    Fk=F1+F2
    F1=Fk
    F2=Fk
    print(Fk, end=" ")
