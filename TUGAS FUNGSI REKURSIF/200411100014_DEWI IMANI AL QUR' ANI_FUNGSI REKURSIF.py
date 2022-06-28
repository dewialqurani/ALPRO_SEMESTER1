def fungsiIteratif(x,n):
    if x==0:
        number=0
    elif n==0:
        number=1
    else:
        number=x
        for i in range(n+1):
            hasil=number**i
            print(x,'pangkat',i,'=',hasil)
            i+=1
    return hasil

def fungsiRekursif(x,n):
    if x==0:
        number=0
    elif n==0:
        number=1
    else:
        number=x*fungsiRekursif(x,n-1)
    return number


print('Fungsi Iteratif')
x=int(input('Masukkan bilangan anda = '))
n=int(input('Masukkan pangkat = '))
fungsiIteratif(x,n)
print('')
print('')
print ('Fungsi Rekursif')
print(x, 'pangkat', n, '=',(fungsiRekursif(x,n)))
