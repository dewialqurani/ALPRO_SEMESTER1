stop=False
while not(stop) :
    print('Menu')
    print('Tekan 1 untuk konversi Desimal ke Biner\nTekan 2 untuk konversi Biner ke desimal')
    pilih=int(input('Masukkan pilihan anda = '))
    if pilih==1 :
        bilangan=int(input('Masukkan Desimal = '))
        totalDiv=bilangan
        Biner=''
        while totalDiv!=0 :
            totalMod=totalDiv%2
            totalDiv=totalDiv//2
            Biner=str(totalMod)+Biner
            print(totalMod)
    elif pilih==2 :
        binstr=input('Masukkan nilai = ')
        pangkat=0
        hasil=0
        for i in range(len(binstr)-1,-1,-1):
            hasil=hasil+int(binstr[i])*2**pangkat
            pangkat+=1
        print(hasil)
    pilihan=input('Ingin mengulang operasi kembali ? click (y/t) : ')
    if pilihan=='y' :
        stop=False
    else :
        stop=True

        