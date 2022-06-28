vocal=0
strvocal=' '
space=' '
spasi=0
strkonsonan=' '
konsonan=0
data=str(input('masukkan kalimat= '))
for i in data:
  if i=='a' or i=='i' or i=='u' or i=='e' or i=='o' or i=='A' or i=='I' or i=='U' or i=='E' or i=='O':
    vocal+=1
    strvocal=strvocal+i
    strvocal=strvocal+' '
  elif i==' ':
    spasi+=1
    space=space+i
  else:
    konsonan=konsonan+1
    strkonsonan=strkonsonan+i
    strkonsonan=strkonsonan+' '
print('jumlah huruf vocal=',vocal, '=',strvocal)
print('jumlah konsonan=',konsonan,'=',strkonsonan)
print('jumlah spasi=',spasi,'=',space)