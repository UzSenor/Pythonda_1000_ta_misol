# For19. n butun son berilgan(n>0). n! ni topuvchi dastur tuzing.
n = int(input("N="))
s=1
if n<=0:
    print("Kiritilgan son nolga teng yoki manfiy")
else:
    for i in range(1, n+1):
        s*=i
        print(i, end=" ")
    print("\nN foktarial: ", s)
