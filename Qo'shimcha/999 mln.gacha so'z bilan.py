# Uyga vazifa 999 mln gacha sonlarni so'z bilan yozish
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

# Birlik
if bir==1:
    bir="bir" 
elif bir==2:
    bir="ikki"
elif bir==3:
    bir="uch"
elif bir==4:
    bir="to'rt"
elif bir==5:
    bir="besh"
elif bir==6:
    bir="olti"
elif bir==7:
    bir="yetti"
elif bir==8:
    bir="sakkiz"
elif bir==9:
    bir="to'qqiz"
else:
    bir=""
    
# O'nlik
if on==1:
    on="o'n"
elif on==2:
    on="yigirma"
elif on==3:
    on="o'ttiz"
elif on==4:
    on="qiriq"
elif on==5:
    on="ellik"
elif on==6:
    on="oltmish"
elif on==7:
    on="yetmish"
elif on==8:
    on="sakson"
elif on==9:
    on="to'qson"
else:
    on=""
    
# Yuzlik
if yuz==1:
    yuz="bir yuz"
elif yuz==2:
    yuz="ikki yuz"
elif yuz==3:
    yuz="uch yuz"
elif yuz==4:
    yuz="to'rt yuz"
elif yuz==5:
    yuz="besh yuz"
elif yuz==6:
    yuz="olti yuz"
elif yuz==7:
    yuz="yetti yuz"
elif yuz==8:
    yuz="sakkiz yuz"
elif yuz==9:
    yuz="to'qqiz yuz"
else:
    yuz=""

    
# Minglik
if ming==0 and (onming!=0 or yuzming!=0):
    ming="ming"
elif ming==1:
    ming="bir ming"
elif ming==2:
    ming="ikki ming"
elif ming==3:
    ming="uch ming"
elif ming==4:
    ming="to'rt ming"
elif ming==5:
    ming="besh ming"
elif ming==6:
    ming="olti ming"
elif ming==7:
    ming="yetti ming"
elif ming==8:
    ming="sakkiz ming"
elif ming==9:
    ming="to'qqiz ming"    
else:
    ming=""

# O'nminglik
if onming==1:
    onming="o'n"
elif onming==2:
    onming="yigirma"
elif onming==3:
    onming="o'ttiz"
elif onming==4:
    onming="qiriq"
elif onming==5:
    onming="ellik"
elif onming==6:
    onming="oltmish"
elif onming==7:
    onming="yetmish"
elif onming==8:
    onming="sakson"
elif onming==9:
    onming="to'qson"
else:
    onming=""

# Yuzminglik
if yuzming==1:
    yuzming="bir yuz"
elif yuzming==2:
    yuzming="ikki yuz"
elif yuzming==3:
    yuzming="uch yuz"
elif yuzming==4:
    yuzming="to'rt yuz"
elif yuzming==5:
    yuzming="besh yuz"
elif yuzming==6:
    yuzming="olti yuz"
elif yuzming==7:
    yuzming="yetti yuz"
elif yuzming==8:
    yuzming="sakkiz yuz"
elif yuzming==9:
    yuzming="to'qqiz yuz"
else:
    yuzming=""
    
# Million
if mln==0 and (onmln!=0 or yuzmln!=0):
    mln="million"
elif mln==1:
    mln="bir million"
elif mln==2:
    mln="ikki million"
elif mln==3:
    mln="uch million"
elif mln==4:
    mln="to'rt million"
elif mln==5:
    mln="besh million"
elif mln==6:
    mln="olti million"
elif mln==7:
    mln="yetti million"
elif mln==8:
    mln="sakkiz million"
elif mln==9:
    mln="to'qqiz million"    
else:
    mln=""
    
# O'nmillion
if onmln==1:
    onmln="o'n"
elif onmln==2:
    onmln="yigirma"
elif onmln==3:
    onmln="o'ttiz"
elif onmln==4:
    onmln="qiriq"
elif onmln==5:
    onmln="ellik"
elif onmln==6:
    onmln="oltmish"
elif onmln==7:
    onmln="yetmish"
elif onmln==8:
    onmln="sakson"
elif onmln==9:
    onmln="to'qson"
else:
    onmln=""
    
# Yuzmillion
if yuzmln==1:
    yuzmln="bir yuz"
elif yuzmln==2:
    yuzmln="ikki yuz"
elif yuzmln==3:
    yuzmln="uch yuz"
elif yuzmln==4:
    yuzmln="to'rt yuz"
elif yuzmln==5:
    yuzmln="besh yuz"
elif yuzmln==6:
    yuzmln="olti yuz"
elif yuzmln==7:
    yuzmln="yetti yuz"
elif yuzmln==8:
    yuzmln="sakkiz yuz"
elif yuzmln==9:
    yuzmln="to'qqiz yuz"
else:
    yuzmln=""
    
print(yuzmln, onmln, mln, yuzming, onming, ming, yuz, on, bir)