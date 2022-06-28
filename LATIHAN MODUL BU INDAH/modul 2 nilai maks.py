#if..elif..else
n1= int(input('masukkan angka pertama ='))
n2= int(input('masukkan angka kedua ='))
n3= int(input('masukkan angka ketiga ='))

if n1>n2 and n1>n3:
    maxNumber=n1
elif n2>n3: 
    maxNumber=n2
else:
    maxNumber=n3
print('nilai maksimal=', maxNumber)
