print('==========SEBELUM BELAJAR BERDOA TERLEBIH DAHULU==========')
print('TUGAS PRAKTIKUM MODUL 2')
print('Nomor 4')
print('*------BILANGAN PRIMA-----*')
print('Bilangan prima adalah bilangan yang hanya dapat dibagi oleh bilangan itu sendiri dan 1')
print('')
print('Diketahui : ')
print('1. Angka 2 adalah bilangan prima')
print('2. Angka 9 adalah bukan  bilangan prima')
print('3. Angka 11 adalah bilangan prima')
print('')
print('Ditanya ?  ')
print('Apakah suatu bilangan adalah bilangan prima atau bukan ? ')
print('')
print('Jawaban : ')
print('')
	
number = int(input('masukkan bilangan  '))
if number > 1:
	for i in range(2,number-1):
		if (number%i)==0:
			print(number, 'adalah bukan bilangan prima')
			break
	else:
		print(number, 'adalah bilangan prima')
else: 
    print(number, 'adalah bukan prima')
print('===========TETAP SEMANGAT JANGAN MENYERAH JANGAN KASIH KENDOR==========')
