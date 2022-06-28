#PENJUMLAHAN LIST 

data_a = []
data_b = []
jumlah = []
panjang = 0

ukuran = int(input("Masukkan ukuran list ke- 1 = "))
for i in range(ukuran):
     print("Masukkan data yang ke-",i,": ",end='')
     list1 = int(input())
     data_a.append(list1)
    
ukuran1 = int(input("Masukkan ukuran list ke- 2 = "))
for i in range(ukuran1):
     print("Masukkan data yang ke-",i,": ",end='')
     list2 = int(input())
     data_b.append(list2)

if len(data_a) > len(data_b):
     panjang= len(data_a)
else:
     panjang = len(data_b)

for i in range(panjang):
     if len(data_a) < len(data_b):
         data_b.append(0)
     elif len(data_b) > len(data_a):
         data_a.append(0)
     total = data_a[i]+ data_b[i]
     jumlah.append(total)

print('List Pertama=',data_a[0:ukuran])
print('List Kedua=',data_b[0:ukuran1])
print('Hasil Penjumlahan=',jumlah)
