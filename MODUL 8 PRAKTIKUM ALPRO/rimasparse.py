from tkinter import *
from tkinter import messagebox

def createSparseMatrix() :
    data = {}
    data["baris"] = int(input("Jumlah Baris = "))
    data["kolom"] = int(input("Jumlah Kolom = "))
    baris = data["baris"]
    kolom = data["kolom"]
    sparse = int(input("jumlah elemen = "))
    i = 1
    while i <= sparse :
        mulai = True
        while mulai :
            iBaris = int(input("Baris ke- ? "))
            if iBaris >= baris :
                messagebox.showerror("Error", "index baris maksimum = {}".format(data["baris"]))
            else :
                mulai = False
        stop = False
        while not stop :
            iKolom = int(input("Kolom ke- ? "))
            if iKolom >= kolom :
                messagebox.showerror("Error", "index kolom maksimum = {}".format(data["kolom"]))
            else :
                stop = True
            
        nilai = int(input("data({},{})= ".format(iBaris,iKolom)))
        data[iBaris,iKolom] = nilai
        i += 1
    
    return (data, baris, kolom )


def addSparseMatrix(data1, data2, baris1, kolom1) :
    addHasil = {}
    mat1 = {}
    mat2 = {}
    for i in range(baris1) :
        for y in range(kolom1) :
            if (i,y) in data1 :
                nilai1 = data1[(i,y)]
                mat1[(i,y)] = nilai1
            else :
                mat1[(i,y)] = 0

    for i in range(baris1) :
        for y in range(kolom1) :
            if (i,y) in data2 :
                nilai2 = data2[(i,y)]
                mat2[(i,y)] = nilai2
            else :
                mat2[(i,y)] = 0
    addHasil["baris"] = baris1
    addHasil["kolom"] = kolom1
    for i in range(baris1) :
        for y in range(kolom1) :
            if mat1[(i,y)] != 0 or mat2[(i,y)] != 0 :
                nilai = mat1[(i,y)] + mat2[(i,y)]
                addHasil[(i,y)] = nilai
            else :
                addHasil[(i,y)] = 0
    return addHasil

def displayData(data, jumlahBaris, jumlahKolom):
    matStr=''
    for i in range(jumlahBaris):
        temp=''
        for j in range(jumlahKolom):
            if (i,j) in data :
                temp=temp+' '+str('%4d'%data[(i,j)])
            else :
                temp=temp+' '+str('%4d'%0)

        temp='%4s'%'|'+temp+'%4s'%'|'
        matStr=matStr+temp+'\n'
    print(matStr)
    print("-------------------")

(matrix1, row1, col1) = createSparseMatrix()
print("Matriks 1 = ", matrix1)
print("-------------------")
(matrix2, row2, col2) = createSparseMatrix()
print("Matriks 2 = ", matrix2)
print("-------------------")
if row1 == row2 and col1 == col2 :
    sum = addSparseMatrix(matrix1, matrix2, row1, col1)
    displayData(matrix1, row1, col1)
    displayData(matrix2, row2, col2)
    displayData(sum, row1, col1)
else :
    messagebox.showerror("Error", "Ukuran Matriks tidak sama")


