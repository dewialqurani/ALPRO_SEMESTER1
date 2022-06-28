#a = Suku awal 
#b = Beda 
#n = Jumlah suku 
#sn = Jumlah bilangan 
#i = bilangan

n = int(input('n = '))
a = int(input('a = '))
b = int(input('b = '))

sn= int((a +(n-1) * b))
for i in range(sn) :
    if a<= sn+1 :
        print(a)
        a=a+b
