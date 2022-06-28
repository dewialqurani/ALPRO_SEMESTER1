def deret(a,b,n):
    if n == 1 :
        return a
    else:
        return  b + deret(a,b,n-1)
a=int(input('Masukkan Suku Awal = '))
b=int(input('Masukkan Beda = '))
n=int(input('Masukkan Banyaknya Suku = '))
hasil=deret(a,b,n)
print("suku ke -",n,"=",hasil)
print('')
print('NAMA : DEWI IMANI AL QUR ANI')
print('NIM : 200411100014')

def total(x,n,z):
    hasil=x*n**z
    return hasil 
x=int(input('Masukkan Angka = '))
n=int(input('Masukkan Angka = '))
z=int(input('Masukkan Pangkat = '))
hasil=total(x,n,z)
print('totalnya adalah  ',hasil)

def total(inisialisasi,num,key):
    gaskun = inisialisasi
    for  in num:
        gaskun+=n
    for k in key:
        gaskun=inisialisasi*num**key
    return gaskun
print(total())
inisialisasi=int(input('Masukkan Angka = '))
num=int(input('Masukkan Angka = '))
key=int(input('Masukkan Pangkat = '))
hasil=total(inisialisasi,num,key)
print('totalnya adalah  ',hasil)