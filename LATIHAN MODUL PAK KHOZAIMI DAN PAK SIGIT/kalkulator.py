def penjumlahan(a, b):
    penjumlahan = float(a) + float(b)
    return penjumlahan

def pengurangan(a, b):
    pengurangan = float(a) - float(b)
    return pengurangan

def perkalian(a, b):
    perkalian = float(a) * float(b)
    return perkalian

def pembagian(a, b):
    pembagian = float(a) / float(b)
    return pembagian

while True :
    print('\n============================================================')
    print('\n===                KALKULATOR SEDERHANA YAP              ===')
    print('\n============================================================')
    a = input('Masukkan Bilangan Pertama : ')
    b = input('Masukkan Bilangan Kedua   : ')
    print('\n1. Penjumlahan\n2.Pengurangan\n3.Perkalian\n4.Pembagian\n5.Keluar')
    c = input('\nMasukkan Pilihan Anda : ')
    if c == '1':
        print('Hasilnya adalah : ',penjumlahan(a, b))
    elif c == '2':
        print('Hasilnya adalah : ',pengurangan(a, b))
    elif c == '3':
        print('Hasilnya adalah : ',perkalian(a, b))
    elif c == '4':
        print('Hasilnya adalah : ',pembagian(a, b))
    elif c == '5':
        break
    else :
        print('Operasi yang Anda Inginkan Tidak Diketahui')