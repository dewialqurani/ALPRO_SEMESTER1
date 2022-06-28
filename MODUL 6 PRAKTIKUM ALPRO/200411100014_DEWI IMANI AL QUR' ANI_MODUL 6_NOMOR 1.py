print('=====  MODUL 6 ALGORITMA PEMROGRAMAN  =====')
print('=====  NOMOR 1 TENTANG FUNGSI REKURSIF DERET ARITMETIKA  =====')
print('')
def deret (a,b,n):
    if n==0:
        return 0
    elif n==1:
        return a
    else:
        hasil = b+deret(a,b,n-1)
        return hasil

a=int(input('Masukkan Suku Awal = '))
b=int(input('Masukkan Beda = '))
n=int(input('Masukkan Banyaknya Suku = '))
hasil=deret(a,b,n)
print("suku ke -",n,"=",hasil)
print('')
print('NAMA : DEWI IMANI AL QUR ANI')
print('NIM : 200411100014')