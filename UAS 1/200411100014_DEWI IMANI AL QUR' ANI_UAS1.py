#NAMA : DEWI IMANI AL QUR' ANI
#NIM : 200411100014
def iteratif(x):
    hasil = 1
    for fak in range(1,x+1):
        hasil=hasil*fak
    return hasil 
def rekursif(x):
    if x==1:
        return 1
    else:
        hasil =x*rekursif(x-1)
        return hasil
rial = True
while rial:
    print('\n1. Tekan 1 untuk memilih fungsi iteratif faktorial \n2. Tekan 2 untuk memilih fungsi rekursif faktorial\n')
    pilih=input('Masukkan apa yang Anda Inginkan = ')
    if pilih =='1':
        number=int(input('Masukkan Angka Anda = '))
        hIteratif=iteratif(number)
        print(hIteratif)
    elif pilih == '2':
        angka=int(input('Masukkan Angka Anda = '))
        hRekursif=rekursif(angka)
        print(hRekursif)
    else:
        print('Angka yang Anda Masukkan Salah. Silahkan Coba lagi!')
    print('Apakah ingin mengulangi program ini ? ')
    print('\n1.Ya\n2.Tidak')
    pilihan = int(input('Masukkan Pilihan Anda = '))
    if pilihan == 1:
        continue
    elif pilihan == 2:
        rial = False



