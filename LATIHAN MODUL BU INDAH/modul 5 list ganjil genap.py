List = []
jumlah = int(input('masukan ukuran list yang pertama = '))
for n in range (jumlah):
  hasil='masukan data ke-'+str(n)+':'
  a=int(input(hasil))
  List.append(a)

ganjil=[i for i in List if i%2==1]
genap=[i for i in List if i%2==0 ]
print(List)
print(ganjil)
print(genap)