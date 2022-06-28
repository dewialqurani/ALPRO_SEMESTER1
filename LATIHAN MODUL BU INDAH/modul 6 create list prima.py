#2.1
ListData=[]
ListPrima=[]
def createList (x):
  for i in range(0,x):
    b=int(input('masukkan data ke - {} : '.format(i)))
    ListData.append(b)
  return ListData
def isiPrime(x):
  count=0
  for y in range(1,x+1):
    if x%y==0:
      count+=1
  if count==2:
    for k in ListPrima:
      if x==k:
        break
    else:
      ListPrima.append(x)
def createlistprima(data):
  for i in data:
    isiPrime(i)
  return ListPrima


data=createList(10)
print('data list = ',data)
prima=createlistprima(data)
print('data prima = ',prima)