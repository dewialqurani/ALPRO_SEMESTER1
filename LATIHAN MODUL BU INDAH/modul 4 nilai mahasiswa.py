 
data=[]
nilai=[]
print('DAFTAR MAHASISWA =')
jumlah = int(input('JUMLAH MAHASISWA ='))
for i in range (1, jumlah+1):
  print('MAHASISWA KE -',i)
  a= input('NAMA MAHASISWA=')
  b= int (input('NIALI MAHASISWA ='))
  data.append(a)
  nilai.append(b)
print('\n 0. DAFTAR MAHASISWA DAN NILAI \n 1. RATA - RATA MAHASISWA \n 2. DAFTAR MAHASISWA YANG MELEBIHI THRESHOLD \n 3. NILAI MAKSIMAL')
menu = int(input('MASUKKAN PILIHAN ANDA='))
if menu == 0:
  nama = len(data and nilai)
  for i in range (nama):
    print(i+1,data[i],nilai[i])
elif menu == 2:
  banyak=0
  score = len(nilai)
  for i in nilai:
    banyak+=1
  print('RATA - RATA =', banyak/score)
elif menu == 3:
  threshold= []
  x = int(input('MASUKKAN TRESHOLD ='))
  for i in nilai:
    if i > x:
      threshold.append(i)
    print('THRESHOLD =', threshold)
elif menu == 4:
  print('NILAI MAKSIMAL =',max(nilai))
else :
  print('MAAF TIDAK ADA MENU YANG ANDA MINTA ^^')
z = input('lagi (y/t)?')
 
 
stop = False
while not(stop):
  if z == 'y':
    stop = False
    print('')
  if z =='t':
    stop=True
    print('')