from tkinter import *
from tkinter import messagebox

#createSparseMatrix()
def createSparseMatrix():
    ordo = {}
    ordo['Baris'] = int(input('Jumlah Baris = '))
    ordo['Kolom'] = int(input('Jumlah Kolom = '))
    baris = ordo['Baris']
    kolom = ordo['Kolom']
    sparMat = int(input('Jumlah Elemen = '))
    i = 1
    while i <= sparMat :
        start = True
        while start :
            iBaris = int(input('Baris ke - ? '))
            if iBaris >= baris :
                messagebox.showerror('Error', 'Indexs Baris Maksimum = {}'.format(ordo['Baris']))
            else :
                start = False
        stop = False
        while not stop :
            iKolom = int(input('Kolom ke - ? '))
            if iKolom >= kolom :
                messagebox.showerror('Error', 'Indexs Kolom Maksimum = {}'.format(ordo['Kolom']))
            else :
                stop = True      
        hasil = int(input('data({},{})= '.format(iBaris,iKolom)))
        ordo[iBaris,iKolom] = hasil
        i += 1
    return (ordo, baris, kolom)

##AddSparseMatrix()
def addSparseMatrix(ordo1, ordo2, baris1, kolom1):
    addSparMat = {}
    mat1 = {}
    mat2 = {}
    for i in range(baris1) :
        for y in range(kolom1) :
            if (i,y) in ordo1 :
                hasil1 = ordo1[(i,y)]
                mat1[(i,y)] = hasil1
            else :
                mat1[(i,y)] = 0

    for i in range(baris1) :
        for y in range(kolom1) :
            if (i,y) in ordo2 :
                hasil2 = ordo2[(i,y)]
                mat2[(i,y)] = hasil2
            else :
                mat2[(i,y)] = 0
    addSparMat['baris'] = baris1
    addSparMat['kolom'] = kolom1

    for i in range(baris1) :
        for y in range(kolom1) :
            if mat1[(i,y)] != 0 or mat2[(i,y)] != 0 :
                hasil = mat1[(i,y)] + mat2[(i,y)]
                addSparMat[(i,y)] = hasil
            else :
                addSparMat[(i,y)] = 0
    return addSparMat

#DisplayData()
def displayData(ordo, jumlahBaris, jumlahKolom):
    matStr=''
    for i in range(jumlahBaris):
        temp=''
        for x in range(jumlahKolom):
            if (i,x) in ordo :
                temp=temp+' '+str('%4d'%ordo[(i,x)])
            else :
                temp=temp+' '+str('%4d'%0)

        temp='%4s'%'|'+temp+'%4s'%'|'
        matStr=matStr+temp+'\n'
    print(matStr)
    print('----------------------------------------------------')

(matrix1, row1, col1) = createSparseMatrix()
print('Matriks 1 = ', matrix1)
print('----------------------------------------------------')
(matrix2, row2, col2) = createSparseMatrix()
print('Matriks 2 = ', matrix2)
print('----------------------------------------------------')
if row1 == row2 and col1 == col2 :
    sum = addSparseMatrix(matrix1, matrix2, row1, col1)
    displayData(matrix1, row1, col1)
    displayData(matrix2, row2, col2)
    displayData(sum, row1, col1)
else :
    messagebox.showerror('Error', 'Ukuran Matriks Tidak Sama')