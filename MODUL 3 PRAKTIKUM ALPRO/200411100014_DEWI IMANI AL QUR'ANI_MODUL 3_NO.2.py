print('=====  MODUL 3 ALGORITMA PEMROGRAMAN  =====')
print('=====  NOMOR 2 TENTANG MENAMPILKAN KONVERSI BILANGAN ASLI KE BILANGAN ROMAWI  =====')
print('')
asli = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romawi = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
bilangan=int(input('masukkan bilangan anda ='))
temp=bilangan
hasil=''

for i in range (len(asli)):
    while bilangan >= asli[i]:
        bilangan-=asli[i]
        hasil+=romawi[i]
print('bilangan asli', temp, 'menjadi bilangan romawi adalah', hasil)
