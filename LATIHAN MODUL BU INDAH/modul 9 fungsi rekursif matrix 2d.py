#create matriks 2D
def creatematriks (baris, kolom):
    a = []
    for i in range(baris):
        b = []
        for x in range (kolom):
            c = int (input(f"mat[{i+1}, {x+1}]:"))
            b.append(c)
        a.append(b)
    return a
    
#display matriks
def displayMatriks(matriks):
    if type(matriks) == str:
        return matriks
    else:
        a = []
        for baris in matriks:
            for kolom in baris:
                a.append(str(kolom))
        b = len (a[0])
        for i in range (1, len (a)):
            if len (a[i]) > b:
                b = len(a[i])
        hasil = ""
        for bar in matriks:
            hasil += "|" + ""*2
            for kol in bar:
                hasil += ""*(b - len(str(kol))) + str(kol) + "" *2
            hasil += "|\n"
        return hasil

#square matriks
def SquareMatriks(matriks):
    if len(matriks) == len (matriks[0]):
        return True
    else:
        return False

#penjumlahan matriks
def penjumlahan (matriks1, matriks2):
    if len (matriks1) != len (matriks2) or (matriks1[0]) != len (matriks2[0]):
        return "tidak sama"
    hasil = []
    panjang = len (matriks1)
    for baris in range (panjang):
        temp = []
        for kolom in range (panjang):
            temp.append(matriks1[baris][kolom] + matriks2[baris][kolom])
        hasil.append(temp)
    return hasil

#perkalian matriks
def perkalian (matriks1, matriks2):
    if len (matriks1) != len (matriks2) != len (matriks2):
        return "tidak sama"
    hasil = []
    for baris1 in range (len(matriks1)):
        a = []
        for baris2 in range (len(matriks2[0])):
            temp = []
            for kolom in range (len(matriks1)):
                temp.append(matriks1[baris1][kolom] * matriks2[baris2][kolom])
            a.append(temp)
        hasil.append(a)
    return hasil

#Nilai Maksimal Matriks
def maksimalMatriks(matriks, x):
    if x == "baris":
        hasil = []
        for baris in range(len(matriks)):
            maksimal = matriks[baris][0]
            for kolom in range (len(matriks[0])):
                if matriks[baris][kolom] > maksimal:
                    maksimal = matriks[baris][kolom]
                hasil.append([maksimal])
    elif x == "kolom":
        hasil = [[]]
        for baris in range (len(matriks)):
            maksimal = matriks[0][baris]
            for kolom in range (len(matriks[0])):
                if matriks[kolom][baris] > maksimal:
                    maksimal = matriks[kolom][baris]
            hasil[0].append(maksimal)
    else:
        maksimal = matriks[0][0]
        for baris in range(len(matriks)):
            for kolom in range(len(matriks[0])):
                if matriks[baris][kolom] > maksimal:
                    maksimal = matriks[baris][kolom]
        hasil = maksimal
    return hasil

print('Data - 1 :')
data1 = creatematriks(3,3)
print('Data - 2 :')
data2 = creatematriks (3,3)

print('Matriks - 1:',displayMatriks(data1), sep='\n')
print('Is Square?',SquareMatriks(data1),'\n')
print('Matriks - 2:',displayMatriks(data2), sep='\n')
print('Is Square?',SquareMatriks(data1),'\n')

jumlah = penjumlahan(data1, data2)
kali = perkalian (data1, data2)
maksimal_1 = maksimalMatriks(data1,'baris')
maksimal_2 = maksimalMatriks(data1,'kolom')
maksimal_3 = maksimalMatriks(data1,'*')

print('Hasil Penjumlahan =',displayMatriks(jumlah),sep='\n')
print('Hasil Perkalian =',displayMatriks(kali),sep='\n')
print('Maksimal - Baris =',displayMatriks(maksimal_1),sep='\n')
print('Maksimal - Kolom =',displayMatriks(maksimal_2),sep='\n')
print('Maksimal =',maksimal_3)

