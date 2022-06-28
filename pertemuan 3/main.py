#PRAKTEK

temp=0
number = int(input('masukkan angka maksimal = '))
for i in range(number) :
    if i%2==1:
        temp=temp+i
        print('bilangan ganjil  =',i)
print('total angka=', temp)


