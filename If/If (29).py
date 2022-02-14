# 29-misol. Butun son berilgan. Berilgan sonni "Musbat toq son", "Manfiy juft son", "Son nolga teng"
# vs h.k. ekranga chiqaradigan dastur tuzing
x = int(input("x = "))
if x>0 and x%2==0:
    print("Son musbat juft")
elif x>0 and x%2==1:
    print("Son musbat toq")
elif x<0 and x%2==0:
    print("Son manfiy juft")
elif x<0 and x%2==1:
    print("Son manfiy toq")
else:
    print("Son nolga teng")