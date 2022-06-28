#program perintah if
nama = 'python'
if nama == 'python':
    print(' hallo '+ nama )

#program perintah if-else
kunci = 'ALLAH'
kata_sandi = input('masukkan kata sandi hati anda = ')
if kata_sandi == kunci :
    print('Kata Sandi yang anda gunakan pada hati anda benar')
else:
    print('Mohon Maaf kata sandi yang anda masukkan salah mohon konfirmasi ulang')

#program perintah if-elif-else
num = int(input('Masukkan angka yang kamu inginka = '))
if num > 0 :
    print(' Angka yang anda masukkan bernilai lebih dari nol ')
elif num < 0 :
    print(' Angka yang anda masukkan bernilai kurang  dari nol ')
else :
    print(' Angka yang anda masukkan bernilai sama dengan  nol ')

#PRAKKTIKUM LATIHAN 1
nomor_acak = 8
print('Tebaklah Angka dibawah ini dari angka 1 - 10')
tebak = int(input('Masukkan angka yang kamu tebak = '))
if tebak == nomor_acak :
    print(' Angka yang anda tebak sangat tepat ')
elif tebak < nomor_acak :
    print(' Angka yang anda tebak kurang tepat karena angka yang anda masukkan terlalu kecil')
else :
    print(' Angka yang anda tebak kurang tepat karena angka yang anda masukkan terlalu besar ')
    print('=== SELESAI ===')

#PRAKKTIKUM LATIHAN 1,A
umur = int(input('Masukkan umur anda sekarang = '))
if umur <= 20 :
    print('MOHON MAAF UMUR ANDA BELUM IDEAL UNTUK MENIKAH ')
elif umur <= 25 :
    print('UMUR ANDA SUDAH MASUK KE UMUR YANG IDEAL UNTUK MENIKAH')
else :
    print('SEMOGA SECEPATNYA ANDA MENDAPATKAN JODOH ANDA SESUAI DENGAN KEINGINAN ANDA')

##PRAKKTIKUM LATIHAN 1,B
angka = int(input('masukkan angka yang anda inginkan = '))
if angka % 2 :
    print('angka yang anda masukkan merupakan bilangan ganjil')
else:
    print('angka yang anda masukkan merupakan bilangan genap')