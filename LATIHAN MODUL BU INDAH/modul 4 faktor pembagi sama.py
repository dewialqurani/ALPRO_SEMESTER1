a = int (input('masukkan angka ke-1='))
b = int (input('masukkan angka ke-2='))
faktor_a=[]
faktor_b=[]
Fpb=[]
for i in range (1, a+1):
  if a % i == 0:
    faktor_a.append(i)
for u in range (1, b+1):
  if b % u == 0:
    faktor_b.append(u)
for i in range (1, a+1 or b+1):
  if b%i==0 and a%i==0 :
    Fpb.append(i)
print('faktor pembagi',a,'=',faktor_a)
print('faktor pembagi',b,'=',faktor_b)
print('FPB',Fpb)