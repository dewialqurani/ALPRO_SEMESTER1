#DERET
n1=1
n2=1
total=0
a=int(input('masukkan angka='))
for i in range(a):
    temp=n1+n2
    n1=n2
    n2=temp
    print(temp)
    total=total+temp
print('total=',total)