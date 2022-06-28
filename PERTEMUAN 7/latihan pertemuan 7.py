#MENCARI NILAI GANJIL
data= [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]
number=0
for i in data:
    if i%2==1:
        number+=i
        print(i)
print('total bilangan ganjil =', number)


#MENCARI RATA RATA
data= [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]
number=0
for i in data:
    number=number+i
rata=number/len(data)
print('rata rata =', rata)


#MENCARI NILAI MAKSIMAL
data= [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]
maksimal=data[0]
for i in range(1,len(data),1):
    if maksimal<data[i]:
        maksimal=data[i]
print('nilai maksimal =',maksimal)

#MENCARI INDEKS
data= [90,56,34,78,86,100,87,88,75,65,86,57,89,67,80]
maksimal=0
indeks=0
for i in data:
    if maksimal<i:
        indeksmaksimal=indeks
        maksimal=i
    indeks=indeks+1
print(maksimal,indeksmaksimal)


#angka dan index di list yg lebih besar dari angka inputan user
data=int(input("masukkan angka : "))
angka=[90, 56, 34, 78, 86, 100, 87, 88, 75, 65, 86, 57, 89, 67, 80]
count=0
nilai_besar=0
ind=0

for i in angka:
    if i>data:
        nilai_besar=i
        print(nilai_besar, "index ke",ind)
    ind+=1 