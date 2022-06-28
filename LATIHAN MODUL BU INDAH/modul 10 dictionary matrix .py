
 
 
#2.1 Create Sparse Matrix 2D
def createSparseMatrix(baris,kolom) :
    objek = {}
    objek["baris"] = baris
    objek["kolom"] = kolom
    data = int(input("jumlah data yang tidak nol ? "))
    if data <= (baris*kolom) and data > 0:
        i = 1
        while i <= data :
            print("data ke-", i)
            aBaris = int(input("Index Baris ke - "))
            aKolom = int(input("Index Kolom ke - "))
            if aBaris < baris and aKolom < kolom and aBaris >= 0 and aKolom >= 0:
                nilai = int(input("sparseMat[{},{}]= ".format(aBaris,aKolom)))
                objek[aBaris,aKolom] = nilai
                i += 1
            else :
                print("index baris atau kolom melebihi jumlah baris atau kolom")
    else :
        print("Jumlah Tidak memenuhi !!!")
    return objek
 
 
#2.2 Display Sparse Matrix 2D
def dispSparseMatrix2D(data):
    jmlhBaris = data["baris"]
    jmlhKolom = data["kolom"]
    matStr=''
    for i in range(jmlhBaris):
        temp=''
        for j in range(jmlhKolom):
            if (i,j) in data :
                temp=temp+' '+str('%4d'%data[(i,j)])
            else :
                temp=temp+' '+str('%4d'%0)
 
        temp='%4s'%'|'+temp+'%4s'%'|'
        matStr=matStr+temp+'\n'
    return (matStr)
 
 
#2.3 Add Sparse Matrix 2D
def addSparseMatrix2D(data1, data2) :
    baris1 = data1["baris"]
    kolom1 = data1["kolom"]
    baris2 = data2["baris"]
    kolom2 = data2["kolom"]
    addJmlh = {}
    mat1 = {}
    mat2 = {}
    for i in range(baris1) :
        for y in range(kolom1) :
            if (i,y) in data1 :
                nilai1 = data1[(i,y)]
                mat1[(i,y)] = nilai1
            else :
                mat1[(i,y)] = 0
 
    for i in range(baris2) :
        for j in range(kolom2) :
            if (i,j) in data2 :
                nilai2 = data2[(i,j)]
                mat2[(i,j)] = nilai2
            else :
                mat2[(i,j)] = 0
 
 
    if baris1 == baris2 and kolom1 == kolom2 :
        addJmlh["baris"] = baris1
        addJmlh["kolom"] = kolom1
        for i in range(baris1) :
            for y in range(kolom1) :
                if mat1[(i,j)] != 0 or mat2[(i,j)] != 0 :
                    nilai = mat1[(i,j)] + mat2[(i,j)]
                    addJmlh[(i,j)] = nilai
                else :
                    addJmlh[(i,j)] = 0
        return addJmlh
    else :
        return False
 
 
#2.4 Multiplication of Sparse Matrix 2D
def multSparseMat(data1, data2) :
    baris1 = data1["baris"]
    kolom1 = data1["kolom"]
    baris2 = data2["baris"]
    kolom2 = data2["kolom"]
    multJumlah = {}
    mat1 = {}
    mat2 = {}
    for i in range(baris1) :
        for j in range(kolom1) :
            if (i,j) in data1 :
                nilai1 = data1[(i,j)]
                mat1[(i,j)] = nilai1
            else :
                mat1[(i,j)] = 0
 
    for i in range(baris2) :
        for j in range(kolom2) :
            if (i,j) in data2 :
                nilai2 = data2[(i,j)]
                mat2[(i,j)] = nilai2
            else :
                mat2[(i,j)] = 0
    if kolom1 == baris2 :
        multJumlah["baris"] = baris1
        multJumlah["kolom"] = kolom2
        for i in range(baris1):
            for k in range(kolom2):
                temp=0
                for l in range(kolom1): 
                    temp=temp+mat1[(i,l)]*mat2[(l,k)]
                multJumlah[(i,k)] = temp
        return multJumlah
    else :
        return False

import SparseMatriks as sm
#2.1
mat1 = sm.createSparseMatrix(5,4)
print(mat1)
print(sm.dispSparseMatrix2D(mat1))
mat2 = sm.createSparseMatrix(5,4)
print(mat2)
print(sm.dispSparseMatrix2D(mat2))
mat3 = sm.createSparseMatrix(4,2)
print(mat3)
print(sm.dispSparseMatrix2D(mat3))
mat4 = sm.createSparseMatrix(1,5)
print(mat4)
print(sm.dispSparseMatrix2D(mat4))
print('Sparse Matriks 1 =')
print(sm.dispSparseMatrix2D(mat1))
print('Sparse Matriks 2 =')
print(sm.dispSparseMatrix2D(mat2))
hasilJumlah=sm.addSparseMatrix2D(mat1,mat2)
if hasilJumlah ==False:
    print('ukuran tidak sama')
else:
    print('hasil Penjumlahan =')
    print(sm.dispSparseMatrix2D(hasilJumlah))
print('Sparse Matriks 1 =')
print(sm.dispSparseMatrix2D(mat1))
print('Sparse Matriks 2 =')
print(sm.dispSparseMatrix2D(mat3))
hasilJumlah=sm.addSparseMatrix2D(mat1,mat3)
if hasilJumlah ==False:
    print('ukuran tidak sama')
else:
    print('hasil Penjumlahan =')
    print(sm.dispSparseMatrix2D(hasilJumlah))
print('Sparse Matriks 1 =')
print(sm.dispSparseMatrix2D(mat3))
print('Sparse Matriks 2 =')
print(sm.dispSparseMatrix2D(mat4))
hasilJumlah=sm.addSparseMatrix2D(mat3,mat4)
if hasilJumlah ==False:
    print('ukuran tidak sama')
else:
    print('hasil Penjumlahan =')
    print(sm.dispSparseMatrix2D(hasilJumlah))
print('Sparse Matriks 1 =')
print(sm.dispSparseMatrix2D(mat3))
print('Sparse Matriks 2 =')
print(sm.dispSparseMatrix2D(mat4))
hasilJumlah=sm.addSparseMatrix2D(mat3,mat4)
if hasilJumlah ==False:
    print('ukuran tidak sama')
else:
    print('hasil Penjumlahan =')
    print(sm.dispSparseMatrix2D(hasilJumlah))
print('Sparse Matriks 1 =')
print(sm.dispSparseMatrix2D(mat1))
print('Sparse Matriks 2 =')
print(sm.dispSparseMatrix2D(mat3))
hasilKali=sm.multSparseMat(mat1,mat3)
if hasilKali ==False:
    print('ukuran tidak memenuhi syarat')
else:
    print('hasil Penjumlahan =')
    print(sm.dispSparseMatrix2D(hasilKali))
print('Sparse Matriks 1 =')
print(sm.dispSparseMatrix2D(mat3))
print('Sparse Matriks 2 =')
print(sm.dispSparseMatrix2D(mat4))
hasilKali=sm.multSparseMat(mat3,mat4)
if hasilKali ==False:
    print('ukuran tidak memenuhi syarat')
else:
    print('hasil Penjumlahan =')
    print(sm.dispSparseMatrix2D(hasilKali))
print('Sparse Matriks 1 =')
print(sm.dispSparseMatrix2D(mat4))
print('Sparse Matriks 2 =')
print(sm.dispSparseMatrix2D(mat1))
hasilKali=sm.multSparseMat(mat4,mat1)
if hasilKali ==False:
    print('ukuran tidak memenuhi syarat')
else:
    print('hasil Penjumlahan =')
    print(sm.dispSparseMatrix2D(hasilKali))
