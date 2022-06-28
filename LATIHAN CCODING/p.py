print("********************************")
print("PROGRAM UNTUK ORANG GABUT/JOMBLO")
print("********************************")
print("Pilih => \n1. Rata2 \n2. Nilai terbesar \n3. Angka terbesar \n4. Lagi (y/t) ?")

data = [90,56,34,78,56,90,87,88,75,65,86,57,89,67,80]
temp = 0
a = 0
while True :
    pilih = input ("Masukkan angka 1 - 4 => ")
    if pilih == "1" :
        for nilai in data:
            if nilai % 2 == 1 :
                a += 1
                temp = temp + nilai
        Rata2 = temp/a
        print("Rata2 =>", Rata2)    
    elif pilih == "2" :
        print('maks =', max(data)) 
    elif pilih == "3" :
        x = int(input("Input Angka => "))
        for i in data:
            if i > x :
                A_besar = i
                print(A_besar, "index ke - ", temp)
                temp+=1
    elif pilih == "4" :
        print("y/t ?")
        ulang = input()
        if ulang == "y":
            pass
        else:
            break
    else:
        print("TERIMAKASIH SAYANG")
        exit()                         