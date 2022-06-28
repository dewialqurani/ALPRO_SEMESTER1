stop=False
while not(stop):
    print('tekan 1 untuk operasi hitung luas lingkaran')
    print('tekan 2 untuk operasi hitung luas persegi panjang')
    print('tekan 3 untuk operasi hitung luas segitiga')
    menu=int(input('masukkan pilihan anda='))
    a=0
    b=0
    if menu==1:
        a=3.14
        b=int(input('jari - jari ='))
        l =a*b*b
        print('Luas lingkaran=',l)
    elif menu==2:
        a =int(input('panjang='))
        b=int(input("lebar="))
        l =a*b
        print('Luas persegi panjang=',l)
    elif menu==3:
        a =int(input("alas="))
        b =int(input("tinggi="))
        l =a*b/2
        print('Luas segitiga=',l)

    inp=input('lagi (y/t)?')
    if inp=='y':
        stop=False
        print('')
    if inp=='t':
        stop=True
        print('')


