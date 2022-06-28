
stop=False
while not(stop):
    print('tekan 1 untuk menghitung deret aritmetika ')
    print('tekan 2 untuk menghitung suku ke n')
    menu=int(input('masukkan pilihan anda='))
    nilai = [89, 87, 67, 89, 54, 67, 78, 84, 54, 65, 67, 88]

    if menu==1:
       for angka in nilai:
            if angka%2==0:
                print(angka, 'adalah bilangan genap')
                
    elif menu==2:
        for angka in nilai:
            if angka%2==1:
                print(angka, 'adalah bilangan ganjil')
                
    inp=input('lagi (y/t)?')
    if inp=='y':
        stop=False
        print('')
    if inp=='t':
        stop=True
        print('')