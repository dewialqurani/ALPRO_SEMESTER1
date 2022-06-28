data = []
genap = []
ganjil = []
prima = []
def createList (a):
    for i in range (a) :
        isi = int(input("Masukkan Bilangan ke- {} : ".format(i)))
        data.append(isi)
    return data
def isiGenap (a) :
    if a % 2 == 0 :
        for i in genap :
            if i == a :
                break
        else :
            return True
    else :
        for i in ganjil :
            if i == a :
                break
        else :
            return False
def isiPrima(a) :
    fact = 0
    for i in range(1, a+1) :
        if a % i == 0 :
            fact += 1
    if fact == 2 :
        for y in prima :
            if y == a :
                break
        else :
            return True
    else :
        return False
x = int(input("Banyaknya Bilangan : "))
lst = createList(x)
print("Bilangan = ",lst)
for i in data :
    cek = isiGenap(i)
    cek2 = isiPrima(i)
    if cek :
        genap.append(i)
    if cek == False :
        ganjil.append(i)
    if cek2 :
        prima.append(i)
print("genap = ", genap)
print("ganjil = ", ganjil)
print("prima = ", prima)               