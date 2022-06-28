
#sequence(runtut)
#konversi celcius ke farenheit

print('==konversi celcius ke farenheit==')

c=int(input('masukkan celcius'))
f=9/5*c+32
print('suhu celcius=',c,'suhu farenheit=',f)


#menghitung luas segitiga

print('==luas segitiga==')

a=int(input('alas='))
t=int(input('tinggi='))

l=1/2*a*t
print('alas=',a,'tinggi=',t,'luas=',l)

#menghitung luas lingkaran

print('==luas lingkaran==')

r=int(input('jari jari='))
l=22/7*r**2
print('jari jari=',r,'luas=',l)

#branching(selection)
# syntax if ke-1 satu cabang
#oddnumber
print('==oddnumber==')
num=int(input('masukkan angka='))
oddnum=None
if num%2==1 :
	oddnum=num
print(oddnum)


#cari nilai max
#tidak indentasi(tab)

print('==maxnumber==')

num1=int(input('masukkan angka-1='))
num2=int(input('masukkan angka-2='))
if num1<num2:
	maxnum=num2
if num1>num2:
	maxnum=num1
print(maxnum)

#indentasi
if num1<num2:
	maxnum=num2
if num1>num2:
	maxnum=num1
	print(maxnum)

#syntax if ke-2 2 cabang
if num1<num2:
	maxnum=num2
else :
	maxnum=num1
print(maxnum)

#maxnum
angka1=int(input('masukkan angka ke-1='))
angka2=int(input('masukkan angka ke-2='))
angka3=int(input('masukkan angka ke-3='))

if angka1>angka2 and angka1>angka3:
	print('maxnum=',angka1)
elif angka2>angka1 and angka2>angka3:
	print('maxnum=',angka2)
else:
	print('maxnum=',angka3)


#syntax if ke-3 percabangan banyak

print('==grade==')

grade=int(input('masukkan nilai='))
if grade>0 and grade<=30:
	print('D')
if grade>30 and grade<=50:
	print('C')
if grade>50 and grade<=80:
	print('B')
if grade >80 and grade<=100:
	print('A')
	
#elif
grade=int(input('masukkan nilai='))
if grade>0 and grade<=30:
	print('D')
elif grade>30 and grade<=50:
	print('C')
elif grade>50 and grade<=80:
	print('B')
else:
	print('A')
	
#Looping(repetition) pengulangan

print('==LOOP==')

for i in range(3):
	print(i)
print('end of iteration')

for i in range(6):
	print(i+5)
print('end of iteration')

#number=int(input('masukkan angka maks='))
for i in range(number):
	if i%2==1:
		print('bilangan ganjil =',i)
print('==range==')
temp=0
number=int(input('masukkan angka maks='))
for i in range(number):
	if i%2==1:
		temp=temp+i
		print('bilangan ganjil =',i)
print('jumlah angka ganjil =',temp)

#2, 4, 6, 8, 10, .....
#un=a+(n-1)b
print('==DERET==')
a=2
b=2
for i in range(10):
	n=i+1
	un=a+(n-1)*b
	print(un)
	
#cara lain deret
print('==DERET==')
for i in range(2,21,2):
	print(i)
	
#cara lain
a=2
for i in range (10):
	print(a)
	a=a+2
	
#cara lain
a=2
temp=0
for i in range(10):
	print(temp)
	temp=temp+a
	a=a+2
print('jumlah=',temp)
