# 36-misol. Birinchi avtomabil tezligi V1 km/soat, ikkinchi avtomabil tezligi V2 km/soat, ular orasidagi masofa S km. Ular bir-biridan uzoqlasha boshlasa T vaqtdan keyin ular orasidagi masofani aniqlaydigan dastur tuzing.
V1 = int(input("Birinchi avtomobil tezligi: "))
V2 = int(input("Ikkinchi avtomobil tezligi: "))
S = int(input("Ular orasidagi masofa: "))
T = int(input("Harakat vaqti: "))
S1 = V1*T
S2 = V2*T
masofa = S+S1+S2
print("Orasidagi masofa: ", masofa, " km")
