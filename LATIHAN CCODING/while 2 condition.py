
stop=False
bilangan=0
counter=1
while counter<=4 and not(stop):
	if bilangan%2==1:
		print('bilangan ganjil ke-',counter,'=',bilangan)
		counter+=1
	else:
		print('bukan bilangan ganjil')
	bilangan+=1
	inp=input('lagi(y/t)?')
	if inp=='y':
		stop=False
	else:
		stop=True
	
	
bilangan=int(input('masukkan angka'))
hasilDiv=bilangan
while hasilDiv:
	hasilDiv=hasilDiv//2
	print(hasilDiv)	
	
			
#div
bilangan=int(input('masukkan angka'))
hasilDiv=bilangan
while hasilDiv:
	hasilMod=hasilDiv%2
	hasilDiv=hasilDiv//2
	print(hasilMod)

bilangan=int(input('masukkan angka'))
hasilDiv=bilangan
strBiner=' '
while hasilDiv:
	hasilMod=hasilDiv%2
	hasilDiv=hasilDiv//2
	strBiner=str(hasilMod)+strBiner
	print('bilangan',strBiner)	