while True :	
	x = int(input("MASUKKAN ANGKA => "))
	if x > 1:
		for i in range(2,x):
			if (x%i)==0:
				print(x, "BUKAN PRIMA")
				break
		else:
			print(x, "PRIMA")
	else:
		print(x, "BUKAN PRIMA")
	print ("=====================")
	print("Coba Lagi ?\n1. Ya\n2. Tidak")
	pilih = int(input("Pilih opsi => "))
	if pilih == 1 :
		continue
	elif pilih == 2 :
		print("THANKS")
		break
	else :
		break
	