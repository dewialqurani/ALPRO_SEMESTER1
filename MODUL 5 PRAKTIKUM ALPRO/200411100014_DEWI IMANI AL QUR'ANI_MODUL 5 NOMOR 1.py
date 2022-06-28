a = []
def createList(x):
    temp = 0
    while (temp < x):
        bilangan = int(input('Masukkan bilangan ke - {} = '.format(temp)))
        a.append(bilangan)
        temp += 1
    print('Bilangan = ', a)
    return a
angka = int(input('Banyaknya Bilangan = '))
createList(angka)

genap  = []
ganjil = []
def isGenap(b):
    if b%2==0:
        for urutan in genap:
            if urutan==b:
                break
        else:
            return True
    else:
        for urutan in ganjil:
            if urutan==b:
                break
        else:
            return False

prima = []
def isPrima(b):
    oke=0
    for urutan in range(1,b+1):
        if b%urutan==0:
            oke += 1
    if oke==2:
        for urutan2 in prima:
            if urutan2==b:
                break
        else :
            return True
    else :
        return False

for i in a:
    lihat = isGenap(i)
    lihat2 = isPrima(i)
    if lihat:
        genap.append(i)
    if lihat==False:
        ganjil.append(i)
    if lihat2:
        prima.append(i)
print('Iki Genap = ', genap)
print('Iki Ganjil = ', ganjil)
print('Iki Prima = ', prima)