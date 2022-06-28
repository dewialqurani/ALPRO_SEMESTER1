a=int(input('masukkan angka='))
total=0

for i in range(1, a + 1) :
    n = i
    un = 1 + (n-1)*2
    print('bilangan ganjil ke-',i, " = ", un)
    total = total + un
    
print('jumlahnya adalah',total)