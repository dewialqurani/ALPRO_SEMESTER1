data = int(input("banyak bilangan = "))
hasil = []
ganjil = []
genap = []
prima = []

for i in range(data):
    hasil.append(int(input("masukkan urutan ke-{}: ".format(i))))

for i in hasil:
    if i%2==0:
        genap.append(i)
    else:
        ganjil.append(i)

print ("list =",hasil)
print ("ganjil =",ganjil)
print ("genap =",genap)
print ("prima =",prima)



List = []
jumlah = int(input('Banyaknya bilangan  = '))
for n in range (jumlah):
  hasil='Masukkan bilangan ke - '+str(n)+'='
  a=int(input(hasil))
  List.append(a)

ganjil=[i for i in List if i%2==1]
genap=[i for i in List if i%2==0 ]
prima=[i for i in List if i%2==0]

print('Bilangan = ', List)
print('Genap = ', genap)
print('Ganjil = ', ganjil)
print('Prima = ', prima)