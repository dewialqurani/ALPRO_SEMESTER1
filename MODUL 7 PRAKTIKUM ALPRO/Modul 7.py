def createMat2D(x,y):
    a = [[] for i in range (x)]
    for i in range (x):
        for j in range (y):
            a[i].append(int(input("Matrix [{}, {}] = ".format(i+1,j+1))))
    return a

def dispMat2D(x,y):
    print(y,x)

def addMat(x,y):
    jumlah = []
    if len(x) == len(y) and len(x[0]) == len(y[0]):
        for b in range(len(x)):
            temp = []
            for k in range(len(x[0])):
                result = x[b][k] + y[b][k]
                temp.append(result)
            jumlah.append(temp)

    else:
        print("Ukuran matriks tidak sama")

    return(jumlah)

def mulMat(x,y):
    kali = []
    if len(x) == len(y) and len(x[0]) == len(y[0]):
        for b in range(len(x)):
            temp1 = []
            for k in range(len(x[0])):
                result1 = x[b][k] * y[b][k]
                temp1.append(result1)
            kali.append(temp1)

    else:
        print("Ukuran Matriks tidak sama")
    
    return(kali)

#Main program
print("Create Mat 1")
Matriks1 = createMat2D(2,3)
print("")
print("Create Mat 2")
Matriks2 = createMat2D(2,3)
print("")
print("Create Mat 3")
Matriks3 = createMat2D(3,2)

print("")
dispMat2D(Matriks1,"Matriks 1 = ")
print("")
dispMat2D(Matriks2,"Matriks 2 = ")
print("")
dispMat2D(Matriks3,"Matriks 3 = ")
print("")
hasilJumlah = addMat(Matriks1,Matriks2)
dispMat2D(hasilJumlah,"Matriks 1 + Matriks 2 = ")
print("")
hasilJumlah1 = addMat(Matriks1,Matriks3)
dispMat2D(hasilJumlah1,"Matriks 1 + Matriks 3 = ")
print("")
hasil1 = mulMat(Matriks1,Matriks2)
dispMat2D(hasil1,"Hasil Matriks 1 * Matriks 2 = ")
print("")
hasil = mulMat(Matriks1,Matriks3)
dispMat2D(hasil,"Hasil Matriks 1 * Matriks 3 = ")