var=int(input('Masukkan bilangan = '))
prima=True
if(var==1):
    prima=False
for i in range (2,var):
	if(var%i==0):
        prima=False
if(prima==True):
    print(var,'adalah bilangan prima')
else:
    print(var,'adalah bukan bilangan prima')
   
 