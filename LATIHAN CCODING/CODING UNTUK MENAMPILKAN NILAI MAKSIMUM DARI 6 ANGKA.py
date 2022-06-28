a=int(input('masukkan angka ke-1='))
b=int(input('masukkan angka ke-2='))
c=int(input('masukkan angka ke-3='))
d=int(input('masukkan angka ke-4='))
e=int(input('masukkan angka ke-5='))
f=int(input('masukkan angka ke-6='))

if a>b and a>c and a>d and a>e and a>f:
	maxnum=a
elif b>a and b>c and b>d and b>d and b>e:
	maxnum=b
elif c>a and c>b and c>d and c>e and c>f:
	maxnum=c
elif d>a and d>b and d>c and d>e and d>f:
	maxnum=d
elif e>a and e>b and e>c and e>d and e>f:
	maxnum=e
else:
	maxnum=f
print('bilangan terbesar=',maxnum)
