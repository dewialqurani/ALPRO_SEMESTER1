print('=====  MODUL 4 ALGORITMA PEMROGRAMAN  =====')
print('=====  NOMOR 2 TENTANG PENJUMLAHAN DUA BUAH MATRIKS =====')
List1 = []
List2 = []
total = []
jumlah1 = int(input('Banyaknya element Matriks - 1  = '))
for n in range (jumlah1):
  hasil1='Masukkan bilangan ke - '+str(n)+' = '
  a=int(input(hasil1))
  List1.append(a)

jumlah2 = int(input('Masukkan banyaknya element Matriks - 2 = '))
for n in range (jumlah2):
  hasil2='Masukkan bilangan ke - '+str(n)+' = '
  a=int(input(hasil2))
  List2.append(a)
if len(List1)==len(List2):
    for i in range (len(List1)):
        total.append(List1[i]+List2[i])
    print('Matriks 1 = ', List1)
    print('Matriks 2 = ', List2)
    print('Matriks 1 + Matrisk 2 = ', total)
elif len(List1)!=len(List2):
    print('Matriks 1 = ', List1)
    print('Matriks 2 = ', List2)
    print('Ukuran Matriks tidak Sama')
