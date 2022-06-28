def createMat2D (x, y) :
    data = []
    for i in range(x) :
        baris = []
        for j in range (y) :
            print('Matriks[',i,',',j,']=',end= '')
            ordo = int(input())
            baris.append(ordo)
        data.append(baris)
    return data
def dispMat2D(a,b) :
    print(b)
    for i in a :
        print('|', end='')
        for y in i :
            print(y, end=' ')
        print('|')
def addMat(a,b):
    baris1 = len(a)
    for i in a :
        baris2 = 0
        for y in i :
            baris2 += 1
    kolom1 = len(b)
    for i in b :
        kolom2 = 0
        for y in i :
            kolom2 += 1
    lst = []
    if kolom1 == baris1 and baris2 == kolom2 :
        i = 0
        for data in a :
            angka = []
            y = 0
            for index in data :
                total = a[i][y] + b [i][y]
                angka.append(total)
                y += 1
            lst.append(angka)
            i += 1
        return lst
    else :
        print('Ukuran Matriks tidak sama')
def multMat (a,b) :
    baris1 = len(a)
    for i in a :
        baris2 = 0
        for y in i :
            baris2 += 1
    kolom1 = len(b)
    for i in b :
        kolom2 = 0
        for y in i :
            kolom2 += 1
    if baris1 == 2 and baris2 == 3 and kolom1 == 3 and kolom2 == 2:
        result = []
        for i in range (2) :
            num = [] 
            for y in range(2) :
                perkalian = ( a[i][0] * b[0][y] ) + ( a[i][1] * b[1][y]) + (a[i][2] * b[2][y])
                num.append(perkalian)
            result.append(num)
        return result
    else :
        print('Ukuran Matriks salah')
print('Create Mat 1')
matriks1 = createMat2D(2,3)
print('')
print('Create Mat 2')
matriks2 = createMat2D(2,3)
print('')
print('Create Mat 3')
matriks3 = createMat2D(3,2)
print('')
hasilJumlah = addMat(matriks1, matriks2)
dispMat2D(matriks1, 'matriks 1 =')
print('')
dispMat2D(matriks2, 'matriks 2 =')
print('')
dispMat2D(matriks3, 'matriks 3 =')
print('')
dispMat2D(hasilJumlah, 'matriks 1 + matriks 2 = ')
hasilJumlah = addMat(matriks1, matriks3)
hasil = multMat(matriks1, matriks3)
dispMat2D(hasil, 'Hasil = ')
hasil = multMat(matriks1, matriks2)


