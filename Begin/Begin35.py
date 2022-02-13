# 35-misol. Qayiqning tezligi V km/soat, Daryo oqimining tezligi U km/soat, (V>U). Qayiqning daryo oqimi bo'yicha harakatlanish vaqti T1, oqimga qarshi T2. Qayiq yurgan S masofani aniqlovchi dastur tuzing.
V = int(input("Qayiqning tezligi: "))
U = int(input("Daryoning tezligi: "))
T1 = int(input("Daryo bo'ylab harakatlanish vaqti: "))
T2 = int(input("Daryoga qarshi harakatlanish vaqti: "))
S1 = (V+U)*T1
S2 = (V-U)*T2
S = S1+S2
print("Bosib o'tgan masofa: ", S, "km")
