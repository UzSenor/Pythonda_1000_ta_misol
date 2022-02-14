# 22-misol. OX va OY kordinata o'qida yotmaydigan nuqta berilgan. Shu nuqtaning qaysi chorakda
# yotishini aniqlaydigan dastur tuzing.
x = int(input("x = "))
y = int(input("y = "))
if x>0 and y>0:
    print("Nuqta birinchi chorakda yotadi")
elif x<0 and y>0:
    print("Nuqta ikkinchi chorakda yotadi")
elif x<0 and y<0:
    print("Nuqta uchinchi chorakda yotadi")
elif x>0 and y<0:
    print("Nuqta to'rtinchi chorakda yotadi")
else:
    print("Nuqta kordinata o'qida yotadi")