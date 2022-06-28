print('==========SEBELUM BELAJAR BERDOA TERLEBIH DAHULU==========')
print('TUGAS PRAKTIKUM MODUL 2')
print('Nomor 2')
print('>-----DERET ARITMETIKA-----<')
suku_awal = int(input('masukkan suku awal   = '))
beda = int(input('masukkan beda     = '))
total = int(input('masukkan total nilai     = '))
print('')
print('DIKETAHUI:')
print('Suku awal    = ',suku_awal)
print('Beda         = ',beda)
print('Total nilai  = ',total)
print('')
print('DITANYA ? ')
print('Biangan suku ke 1-5')
print('Total nilai bilangan tiap barisnya')
print('')
print('JAWABAN : ')
print('')
a=suku_awal
number=0
total_nilai=a
while total_nilai<=total:
    number=number+1
    print('suku ke-',number,'=',a,'total= ',total_nilai)
    a=a+beda
    total_nilai=total_nilai+a
print('===========TETAP SEMANGAT JANGAN MENYERAH JANGAN KASIH KENDOR==========')