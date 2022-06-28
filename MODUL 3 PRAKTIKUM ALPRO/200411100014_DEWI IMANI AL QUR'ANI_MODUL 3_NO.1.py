print('=====  MODUL 3 ALGORITMA PEMROGRAMAN  =====')
print('=====  NOMOR 1 TENTANG MENAMPILKAN BILANGAN BILANGAN PEMBAGI YANG SAMA  =====')
x=[]
y=[]
number= int(input('masukkan bilangan pertama = '))
nomor= int(input('masukkan bilangan pertama = '))
temp=0
maxs=0
for i in range(2,number+1):
    if number%i==0:
        x.append(i)
for i in range(2,nomor+1):
    if nomor%i==0:
        y.append(i)
for i in y :
    if i in x:
        temp+=+
        maxs=i
        print('Pembagi yang sama- ', temp, '=', maxs)  
print('Pembagi yang sama yang Terbesar adalah','=', maxs)      