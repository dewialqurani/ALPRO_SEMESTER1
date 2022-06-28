print('=====  MODUL 6 ALGORITMA PEMROGRAMAN  =====')
print('=====  NOMOR 2 TENTANG FUNGSI REKURSIF MENGHITUNG BILANGAN EXPONENSIAL  =====')
print('')
def expNumberIteratif(x,n):
    if x==0:
        num=0
    elif n==0:
        num=1
    else:
        for i in range(n+1):
            hasil=x**i
            i+=1
        num=hasil
    return num

def expNumberRekursif(x,n):
    if x==0:
        num=0
    elif n==0:
        num=1
    else:
        num=x*expNumberRekursif(x,n-1)
    return num

x=int(input('Masukkan Angka = '))
n=int(input('Masukkan pangkat = '))
print()
print ('Fungsi Iteratif')
h=expNumberIteratif(x,n)
print(x,'pangkat',n,'=',h)
print()
print ('Fungsi Rekursif')
t=expNumberRekursif(x,n)
print(x,'pangkat',n,'=',t)
print('')
print('NAMA : DEWI IMANI AL QUR ANI')
print('NIM : 200411100014')