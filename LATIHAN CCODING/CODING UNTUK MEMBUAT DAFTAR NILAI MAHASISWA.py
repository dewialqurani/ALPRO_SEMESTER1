nama = []
nilai = []
print('pendataan mahasiswa')
jml = int(input(' jumlah mahasiswa = '))
for x in range (1,jml+1):
    print('mahasiswa ke- ', x)    
    inp_nama=str(input('masukkan nama mahasiswa => '))
    inp_nilai=int(input('masukkan nilai mahasiswa => '))
    nama.append(inp_nama)
    nilai.append(inp_nilai)

print('*******************************')

while True:
    print("Data Nilai Mahasiswa: \n1.daftar nama mahasiswa dan nilainya \n2.rata rata \n3.daftar mahasiswadengan nilai lebih dari thresold \n4. nilai tertinggi")
    pilih = input ('angka 1 - 4 : ')
    if pilih == '1':
        name = len(nama and nilai)
        for i in range(name):
            print(i+1,'.', nama[i], '\t=', nilai[i])
    elif pilih == '2' :
        total = 0
        score = len(nilai)
        for i in nilai:
            total += i
        print('nilai rata2 mahasiswa = ', total/score)
    elif pilih == '3':
        trs=[]    
        inp = int(input('nilai thresold = '))
        for i in nilai:
            if i > inp:
                trs.append(i)
        print('nilai thresold :', trs)        
    elif pilih == '4':
        print('maks =', max(nilai))
    else:
        break      