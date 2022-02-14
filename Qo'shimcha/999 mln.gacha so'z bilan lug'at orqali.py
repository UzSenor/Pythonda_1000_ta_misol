# Uyga vazifa 999 mln. ikkinchi variant
s = int(input("999 mln. gacha son kiriting:"))

bir = s%10
on = s%100//10
yuz = s%1000//100
ming = s%10000//1000
onming = s%100000//10000
yuzming = s%1000000//100000
mln = s%10000000//1000000
onmln = s%100000000//10000000
yuzmln = s//100000000

birlik={1:"bir", 2:"ikki", 3:"uch", 4:"to'rt", 5:"besh", 6:"olti", 7:"yetti", 8:"sakkiz", 9:"to'qqiz", 0:""}
onlik={1:"o'n", 2:"yigirma", 3:"o'ttiz", 4:"qiriq", 5:"ellik", 6:"oltmish", 7:"yetmish", 8:"sakson", 9:"to'qson", 0:""}
yuzlik={1:"bir yuz", 2:"ikki yuz", 3:"uch yuz", 4:"to'rt yuz", 5:"besh yuz", 6:"olti yuz", 7:"yetti yuz", 8:"sakkiz yuz", 9:"to'qqiz yuz", 0:""}
minglik={1:"bir ming", 2:"ikki ming", 3:"uch ming", 4:"to'rt ming", 5:"besh ming", 6:"olti ming", 7:"yetti ming", 8:"sakkiz ming", 9:"to'qqiz ming", 0:""}
onminglik={1:"o'n", 2:"yigirma", 3:"o'ttiz", 4:"qiriq", 5:"ellik", 6:"oltmish", 7:"yetmish", 8:"sakson", 9:"to'qson", 0:""}
yuzminglik={1:"bir yuz", 2:"ikki yuz", 3:"uch yuz", 4:"to'rt yuz", 5:"besh yuz", 6:"olti yuz", 7:"yetti yuz", 8:"sakkiz yuz", 9:"to'qqiz yuz", 0:""}
mlnlik={1:"bir million", 2:"ikki million", 3:"uch million", 4:"to'rt million", 5:"besh million", 6:"olti million", 7:"yetti million", 8:"sakkiz million", 9:"to'qqiz million", 0:""}
onmlnlik={1:"o'n", 2:"yigirma", 3:"o'ttiz", 4:"qiriq", 5:"ellik", 6:"oltmish", 7:"yetmish", 8:"sakson", 9:"to'qson", 0:""}
yuzmlnlik={1:"bir yuz", 2:"ikki yuz", 3:"uch yuz", 4:"to'rt yuz", 5:"besh yuz", 6:"olti yuz", 7:"yetti yuz", 8:"sakkiz yuz", 9:"to'qqiz yuz", 0:""}

if ming==0:
    minglik[ming]="ming"
if yuzming==0 and onming==0 and ming==0:
    minglik[ming]=""
if mln==0:
    mlnlik[mln]="million"
if yuzmln==0 and onmln==0 and mln==0:
    mlnlik[mln]=""

print(yuzmlnlik[yuzmln],onmlnlik[onmln],mlnlik[mln],yuzminglik[yuzming],onminglik[onming],minglik[ming],yuzlik[yuz],onlik[on],birlik[bir])