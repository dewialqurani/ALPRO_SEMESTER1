a = int(input('masukkan bilangan anda='))
factor_pembagi=0
factor=[]
b=1
while b <=a:
  if(a%b)==0:
    factor_pembagi=factor_pembagi+1
    factor.append(b)
  b=b+1
print('faktor pembagi dari',a,'adalah',factor)