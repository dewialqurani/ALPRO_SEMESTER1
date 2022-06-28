print('====looping while====')
i=0
while i<=5:
	print(i)
	i=i+1
print('end of while')

print('====syntax while====')

i=3
while i>=3 and i<=10:
	print(i)
	i=i+1 #i=i+1 == #i+=1
print('end of while')

print('===ganjil while===')		
		
i=0		
while i<=5:
	if i%2==1:
		print(i)
	i+=1
print('end of while')

print('====bilangan ganjil pertama====')
bilangan=0
counter=1
while counter<=5:
	if bilangan%2==1:
		print('bilangan ganjil ke-',counter,'=',bilangan)
		counter+=1
	bilangan+=1
print('end of while')

print('=inputan user=')

stop=False
while not(stop):
	inp=input('lagi(y/t)?')
	if inp=='y':
		stop=False
	else:
		stop=True
