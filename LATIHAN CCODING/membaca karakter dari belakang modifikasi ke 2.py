binStr =input('masukkan biner = ')
pangkat = 0
hasil = 0
for i in range(len(binStr)-1,-1,-1): #menggunakan 3 parameter (awal,akhir,interval)
    print(binStr[i],pangkat) 
    hasil=hasil+int(binStr[i])*2**pangkat
    pangkat+=1
print(hasil)