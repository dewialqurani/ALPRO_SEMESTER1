uang =[100000, 50000, 20000, 10000, 5000, 2000, 1000]
strUang =['seratus ribu', 'limapuluh ribu', 'duapuluh ribu', 'sepuluh ribu', 'lima ribu', 'dua ribu', 'seribu']
rupiah = int(input('Masukkan Uang : '))
sisa = rupiah
stop = False
indUang=0
while not(stop):
    bagi=sisa//uang[indUang]
    print(bagi, 'Lembar', strUang[indUang])
    sisa=sisa%uang[indUang]
    if sisa ==0:
        stop = True
    indUang+=1