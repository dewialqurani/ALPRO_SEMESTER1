a=int(input('masukkan angka ke-1='))
b=int(input('masukkan angka ke-2='))
c=int(input('masukkan angka ke-3='))
d=int(input('masukkan angka ke-4='))

if a>b:
	maxnum=a
if b>a:
	maxnum=b
if c>b:
	maxnum=c
if d>c:
	maxnum=d
print('maxnum=',maxnum)


if a>b:
	maxnum1=a
else:
	maxnum1=b
if c>d:
	maxnum2=c
else:
	maxnum2=d
if maxnum1>maxnum2:
	maxnum=maxnum1
else:
	maxnum=maxnum2
print('maxnumber=',maxnum)