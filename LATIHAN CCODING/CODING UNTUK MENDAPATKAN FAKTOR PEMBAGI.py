data=[]
bilangan=int(input('masukkan bilangan = '))
for a in range(1,bilangan+1):
    if bilangan%a == 0:
        data.append(a)
print('faktor pembagi dari', bilangan, '=', data)        