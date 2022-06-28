#BILANGAN PRIMA

a=int(input("masukkan bilangan ="))
faktor=0
for i in range(a):
    if a%(i+1)==0:
        faktor+=1
if faktor==2:
    print(a,'bilangan prima')
else:
    print(a,'bukan bilangan prima, karena memiliki jumlah faktor pembagi sebanyak',faktor)