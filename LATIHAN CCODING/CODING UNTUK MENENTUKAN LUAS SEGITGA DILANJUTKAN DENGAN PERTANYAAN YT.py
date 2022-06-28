 print("Mengitung luas segitiga")

alas = int(input("Masukkan alas : "))
tinggi = int(input("Masukkan tinggi : "))


if 0 < alas < 100 and 0 < tinggi < 100 :

    luas = int(0.5*alas*tinggi)
    print("Luas segitiga adalah ",luas)

else :
    print("MASUKKAN ANGKA ANTARA 0 - 100")


while True :
    jawab = str(input("Apakah dewi ingin mengulang lagi ?"))
    if jawab ==("Y") :

        alas = int(input("Masukkan alas : "))
        tinggi = int(input("Masukkan tinggi : "))


        if 0 < alas < 100 and 0 < tinggi < 100 :

            luas = int(0.5*alas*tinggi)
            print("Luas segitiga adalah ",luas)

        else :
            print("MASUKKAN ANGKA ANTARA 0 - 100")

    elif jawab ==("T") :
        print ("Terimakasih telah menggunakan program ini")
        break

    else :
        print ('WARNING !!! masukkan "Y" atau "T"')

