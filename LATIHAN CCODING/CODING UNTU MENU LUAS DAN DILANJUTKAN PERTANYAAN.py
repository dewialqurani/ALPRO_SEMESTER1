print("Program Menghiting Luas")
print("*************************")
print("Pilih: \n1. Lingkaran \n2. Persehi Panjang \n3. Segitiga \n4. Keluar")

while True:
	pilih = input ("Masukkan angka 1 - 4 : ")
	if  pilih == "1" :
		r = int(input("Masukkan Jari-Jari : "))
		phi = 22/7
		Luas = phi * r * r
		print("Luas Lingkaran adalah : ", Luas)
	elif pilih == "2":
		p = int(input("Masukkan Panjang : "))
		l = int(input("Masukkan Lebar : "))
		Luas = p * l
		print("Luas Persegi Panjang = ", Luas)
	elif pilih == "3" :
		a = int(input("Masukkan Alas : "))
		t = int(input("Masukkan Tinggi : "))
		Luas = 1/2 * a * t
		print("Luas segitiga adalah : ", Luas)
	elif pilih == "4" :
		print("Terima kasih")
		exit()
	print("Lagi? y/t")
	pilih = str(input("Pilih; => "))
	if pilih == "y" :
		continue
	elif pilih == "t" :
		print("TETAP MENYERAH DAN JANGAN SEMANGAT")
		break