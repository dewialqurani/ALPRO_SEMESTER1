angka=int(input('masukkan angka 1-9: '))
x=1,2,3,4,5,6,7,8,9

if 1<=angka<5:
    print(x[:4])
elif 9>=angka>=5:
    print(x[4:])
else:
    print('MAAF ANGKA TIDAK TERDAFTAR')