def createSparseMatrix(baris,kolom):
  sperMat = {'baris' : baris, 'kolom' : kolom }
  numData = int(input('jumlah data yang tidak 0 = '))
  cek = 0
  temp = 1
  while cek != numData:  
      print('data ke - ',temp)
      Isbaris =int(input('jumlah Baris = '))
      Iskolom =int(input('jumlah kolom - '))
      Indeks_baris = baris - 1
      Indeks_kolom = kolom - 1
      if Isbaris < baris:
        if Iskolom < kolom:
          txt = "SeperseMat["+str(Isbaris)+','+str(Iskolom)+"]="
          sperMat[Isbaris ,Iskolom]=int(input(txt))
          cek += 1
          temp += 1
        else:
          print('Indeks baris atau kolom melebihi jumlah baris dan kolom')  
      else:
        messagebox.showerror('Error', 'ukuran matriks tidak sama') 

  return sperMat

a =int(input('masukkan angka untuk kolom = '))
b =int(input('masukkan angka untuk baris = '))
mat1 =createSparseMatrix(a,b)
print(mat1)
print(displayMatrix2D(mat1))
