print ("Selamat datang di program ini")
nama=str(input("masukkan nama anda =" ))
nim =int(input("masukkan NIM anda =" ))
UTS =int(input("masukkan nilai UTS =" ))
UAS = int(input("masukkan nilai UAS =" ))
print ("Nama anda :" ,nama)
print ("NIM Anda :" , nim)
rata_rata = (UTS + UAS)/2
print("Nilai rata-rata Anda :" , rata_rata)
if 100>= rata_rata >=80  :
    print("Anda mendapatkan Nilai A")
elif 80> rata_rata >=70 :
    print ("Anda mendapatkan Nilai B" )
elif 70> rata_rata >=60 :
    print ("Anda mendapatkan Nilai C" )
elif 60> rata_rata >=40 :
    print ("Anda mendapatkan Nilai D" )
else :
     print ("Anda mendapatkan Nilai E" )





