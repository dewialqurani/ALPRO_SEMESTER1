#menentukan jumlah huruf vokal
nilai=[]
data=input("masukkan data=")
nilai=data
nilai=nilai.lower()
data_vokal=[]
data_konsonan=[]
banyak_vokal=0
banyak_konsonan=0
spasi=0
for ch in data:
  if ch=="a" or ch=="i" or ch=="u" or ch=="e" or ch=="o" :
    banyak_vokal=banyak_vokal+1
    data_vokal.append(ch)
  elif ch==" ":
    spasi=spasi+1
  else:
    banyak_konsonan=banyak_konsonan+1
    data_konsonan.append(ch)
print("banyak huruf vokal =", banyak_vokal, "adalah =", data_vokal)
print("banyak huruf konsonan =", banyak_konsonan, "adalah =", data_konsonan)
print("spasi =", spasi)

