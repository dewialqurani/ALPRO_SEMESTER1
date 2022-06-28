def name(nama):
    print(nama)
name('DEWI IMANI AL QUR ANI')
print('')
saya = input('Masukkan kata anda = ')
name(saya)
print('')
print('')
def name():
    print('DEWI IMANI AL QUR ANI')
name()
print('')
def bilangan_aritmetika():
    x = int(input('masukkan bilangan pertama = '))
    y = int(input('masukkan bilangan kedua = '))
    total=x*y
    print(total)
bilangan_aritmetika()
print('')
def bilangan_aritmetika2(x,y):
    total=x+y
    print('hasil dari fungsi adalah ', total)
    return total
print(bilangan_aritmetika2(7,3)*8)