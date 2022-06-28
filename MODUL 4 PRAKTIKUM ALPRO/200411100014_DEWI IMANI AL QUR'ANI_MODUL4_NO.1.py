print('=====  MODUL 4 ALGORITMA PEMROGRAMAN  =====')
print('=====  NOMOR 1 TENTANG MENAMPILKAN TIGA BUAH LIST YANG BERISI BILANGAN GENAP, GANJIL, DAN PRIMA  =====')
print('')
total = int(input('Banyaknya Bilangan  = '))
a = []
temp = 0
while (temp < total):
    number = int(input('Masukkan bilangan ke - {} = '.format(temp)))
    a.append(number)
    temp += 1
print('Bilangan = ', a)

genap = [index for index in a if index%2 == 0]
genap = list(dict.fromkeys(genap))
print('Genap = ', genap)

ganjil = [index for index in a if index%2 == 1]
ganjil = list(dict.fromkeys(ganjil))
print('Ganjil = ', ganjil) 
 
prima = [index for index in a
               if (index==2 or index==3 or index==5 or index==7) or (index%2 != 0  and index%3 != 0 and index%5 != 0 and index%7 != 0)]
prima = list(dict.fromkeys(prima))
print('Prima = ', prima)