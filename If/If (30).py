# 30-misol. 1-999 oraliqda son berilgan. Berilgan sonni "Ikki xonali juft son", "Uch xonali toq son"
# va x.k.ekranga chiqaradigan dastur tuzing.
a = int(input("a (1-999) = "))
if a//100==0 and a//10==0 and a%10!=0 and a%2==0:
    print("Bir xonali juft son")
elif a//100==0 and a//10==0 and a%10!=0 and a%2==1:
    print("Bir xonali toq son")
elif a//100==0 and a%100!=0 and a%2==0:
    print("Ikki xonali juft son")
elif a//100==0 and a%100!=0 and a%2==1:
    print("Ikki xonali toq son")
elif a//100>0 and a//1000==0 and a%2==0:
    print("Uch xonali juft son")
elif a//100>0 and a//1000==0 and a%2==1:
    print("Uch xonali toq son")
elif a//1000>0:
    print("Siz uch xonalidan katta son kiritdingiz")
else:
    print("Son nolga teng")
    
 # 30-misol. 1-999 oraliqda son berilgan. Berilgan sonni "Ikki xonali juft son", "Uch xonali toq son"
# va x.k.ekranga chiqaradigan dastur tuzing.
a = int(input("a (1-999) = "))
bir = a%10
un = a%100//10
yuz = a//100
ming = a//1000
if un>bir>0 and a%2==0:
    print("Bir xonali juft son")
elif un>bir>0 and a%2==1:
    print("Bir xonali toq son")
elif yuz>un>0 and a%2==0:
    print("Ikki xonali juft son")
elif yuz>un>0 and a%2==1:
    print("Ikki xonali toq son")
elif ming>yuz>un and a%2==0:
    print("Uch xonali juft son")
elif ming>yuz>un and a%2==1:
    print("Uch xonali toq son")
elif ming>0:
    print("Siz uch xonalidan katta son kiritdingiz")
else:
    print("Son nolga teng")