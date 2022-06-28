print('ROKET 2020')
print('MISSION 2')
print('KELOMPOK GUMIHO')
print('')
g=int(input('Masukkan angka ke - 1 = '))
u=int(input('Masukkan angka ke - 2 = '))
m=int(input('Masukkan angka ke - 3 = '))
i=int(input('Masukkan angka ke - 4 = '))
h=int(input('Masukkan angka ke - 5 = '))

if g>u and g>m and g>i and g>h:
	maxnum=g
elif u>g and u>m and u>i and u>h:
	maxnum=u
elif m>g and m>u and m>i and m>h:
	maxnum=m
elif i>g and i>u and i>m and i>h:
	maxnum=i
else:
	maxnum=h
print('Bilangan terbesar = ',maxnum)
