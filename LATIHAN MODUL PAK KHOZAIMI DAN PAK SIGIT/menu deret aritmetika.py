stop=False
while not(stop):
    print('tekan 1 untuk menghitung deret aritmetika ')
    print('tekan 2 untuk menghitung suku ke n')
    menu=int(input('masukkan pilihan anda='))
    a= int(input('masukkan suku awal = '))
    b= int(input('masukkan beda = '))
    n=int(input('masukkan suku ke n = '))
    if menu==1:
        un=a+(n-1)*b
        print('deret aritmetika =',un)
    elif menu==2:
        sn=(n/2)*(a+(a+(n-1)*b))
        print('jumlah suku ke n = ', sn)

    inp=input('lagi (y/t)?')
    if inp=='y':
        stop=False
        print('')
    if inp=='t':
        stop=True
        print('')