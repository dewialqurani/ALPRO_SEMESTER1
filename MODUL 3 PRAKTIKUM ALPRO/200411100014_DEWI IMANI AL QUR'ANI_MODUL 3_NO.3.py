print('=====  MODUL 3 ALGORITMA PEMROGRAMAN  =====')
print('=====  NOMOR 3 TENTANG MENAMPILKAN KONVERSI BILANGAN ROMAWI KE BILANGAN ASLI =====')
asli = {'I': 1, 'IV': 4, 'V': 5, 'IX':  9, 'X': 10, 'XL':40, 'L': 50, 'XC':90, 'C': 100, 'CD':400, 'D': 500, 'CM':900, 'M': 1000}
bilangan = str(input('Masukkan romawi Anda = '))
hasil=0  
for i in range (len(bilangan)):
    if i == 0 or asli[bilangan[i]] <= asli[bilangan[i - 1]]:
        hasil += asli[bilangan[i]]
    else:
        hasil+= asli[bilangan[i]] - 2 * asli[bilangan[i - 1]] 
print('bilangan romawi', bilangan, 'menjadi bilangan asli adalah', hasil)