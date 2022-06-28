#Mendapatkan nama hari dari suatu tanggal

hari1 = ('minggu','senin','selasa','rabu','kamis','jumat','sabtu')
hari2 = ('senin','selasa','rabu','kamis','jumat','sabtu','minggu')
hari3 = ('selasa','rabu','kamis','jumat','sabtu','minggu','senin')
hari4 = ('rabu','kamis','jumat','sabtu','minggu','senin','selasa')
hari5 = ('kamis','jumat','sabtu','minggu','senin','selasa','rabu')
hari6 = ('jumat','sabtu','minggu','senin','selasa','rabu','kamis')
hari7 = ('sabtu','minggu','senin','selasa','rabu','kamis','jumat')

temp =('')
a = str(input('Masukkan informasi, hari pertama bulan ini, jatuh pada hari : ')).lower()
b = int(input('Masukkan tanggal yang ingin di ketahui harinya : '))

if a == 'minggu':
    temp = hari1
elif a  == 'senin':
    temp = hari2
elif a == 'selasa':
    temp = hari3
elif a == 'rabu':
    temp = hari4
elif a == 'kamis':
    temp = hari5
elif a == 'jumat':
    temp = hari6
elif a == 'sabtu':
    temp = hari7


mod = b%7
if mod > 7:
    print('Tanggal',b,'Adalah Hari',temp[mod])
else:
    print('Tanggal',b,'Adalah Hari',temp[mod-1])