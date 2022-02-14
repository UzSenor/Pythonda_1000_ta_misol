# 18-misol. Sonlar o'qida a, b, c nuqtalar berilgan. c nuqta a va b nuqtalar orasida joylashgan. ac va bc kesmalar uzunligining ko'paytmasini toping.
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
ac = abs(c-a)
bc = abs(b-c)
kupaytma = ac*bc
print("Ko'paytma: ", kupaytma)