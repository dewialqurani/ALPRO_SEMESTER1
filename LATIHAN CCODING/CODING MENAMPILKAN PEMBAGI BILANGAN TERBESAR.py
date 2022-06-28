a=[]
b=[]
c= int(input('masukkan bilangan pertama = '))
d= int(input('masukkan bilangan kedua = '))
temp=0
maksimal=0
for i in range(2,c+1):
    if c%i==0:
        a.append(i)
for i in range(2,d+1):
    if d%i==0:
        b.append(i)
for i in b :
    if i in a:
        temp+=1
        maksimal=i
        print('pembagi yang sama- ', temp, '=', maksimal)  
print('pembagi yang sama yang terbesar adalah', maksimal)      