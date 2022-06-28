bil=0
counter=1
temp=0
while counter<=10:
	if bil%2==1:
		temp=temp+bil
		print('bilangan ganjil ke-',counter,'=',bil)
		counter+=1
	bil+=1
print('jumlah bilangan ganjil = ',temp)


#4,7,10,...
#un=a+(n-1)*b

a=4
b=3
temp=0
number=int(input('masukkan number = '))
for i in range(number):
	n=i+1
	un=a+(n-1)*b
	temp=temp+un
	print('u-',n,'=',un)
print('jumlah suku = ',temp)



a=4
b=3
temp=0
number=int(input('masukkan number = '))
for i in range(number):
	n=i+1
	un=a+(n-1)*b
	temp=temp+un
	print('u-',n,'=',un)
print('jumlah suku = ',n/2*(2*a+(n-1)*b))