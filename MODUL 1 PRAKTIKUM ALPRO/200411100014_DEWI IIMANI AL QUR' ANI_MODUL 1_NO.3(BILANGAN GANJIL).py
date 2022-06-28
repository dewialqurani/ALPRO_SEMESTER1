bilangan=0
a=int(input('masukkan jumlah angka ganjil = '))
number=1
while number<=a:
    if bilangan%2==1:
      print('bilangan ganjil ke-',number,'=',bilangan)
      number+=1
    bilangan+=1
print('total angka=', number) 
