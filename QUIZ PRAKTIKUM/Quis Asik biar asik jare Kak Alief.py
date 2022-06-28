def total(inisialisasi =5,*num,**key):
    gaskun = inisialisasi
    for n in num:
        gaskun*=n
    for k in key:
        gaskun=gaskun*num**key
    return gaskun
print('')
print(total(5,51,1))
print('')
print('')
print('1. Nilai yang dibutuhkan untuk mendapatkan hasil 255 jika x*y**z adalah 5,51,1.Jika 5 * 51 ** 1 maka hasilnya 255.')
print('2. Menurut saya program yang diberikan pada quiz asik ini ada kekurangan dan kesalahan. Pada gaskun + = n, biasanya menggunakan gaskun * = n karena pada program tersebut diminta suatu perkalian bukan banyaknya perulangan atau iterasi. Pada perulangan k sama halnya dengan perulangan di n tidak usah menggunakan tanda + karena yan diminta bukan iterasi hanya diminta untuk menampilkan hasil dari suatu nilai. Pada parameter ditentukan sebuah operasi perkalian dan perpangkatan jadi pada perulangan k ini kita masukkan rumus agar sesuai dengan output yang diinginkan seperti gaskun*num**key, mengapa menggunakan gaskun kok bukan parameter inisialisasi yang telah disediakan sebenarnya sama saja tidak ada bedanya karena diatas telah diketahui bahwa gaskun = inisialisasi jadi tidak akan berpengaruh entah menggunakan inisialisasi ataupun gaskun. Lalu bagaimana agar output menghasilkan angka 255, jadi kita menggunakan nilai 5,51,1 karena pembagi dari angka 255 itu ada 1,3,5,15,17,51,85,255 pada angka pembagi tersebut tidak ada angka yang bisa dipangkatkan jika dikali 5 dulu  agar menghasilkan angka 255 selain angka 1, jadi saya menggunakan angka 5 * 51 **1 ')
print('')
print('')
print('NAMA : DEWI IMANI AL QUR ANI')
print('NIM : 200411100014')