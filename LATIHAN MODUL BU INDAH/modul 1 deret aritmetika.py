a = float(input('Masukkan Suku-1='))
b = float(input('Masukkan pembeda='))
c = int(input('masukkan suku ke='))
temp=0
for i in range(1, c+1):
    n=i
    un=a+(n-1)*b
    print('un',i,'=',un)
    temp=temp+1
print('Total=', temp)
sn=(n/2)*(a+un)
print('sn=',sn)