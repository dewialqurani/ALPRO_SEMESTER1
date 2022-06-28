#Deret Aritmatika Rekursif
def deret (a,b,n):
    if (n == 0):
        return(0)
    elif (n == 1):
        return(a)
    else:
        hasil = b + deret(a,b,n-1)
        return(hasil)

a = int(input("Suku awal (a)    : "))
b = int(input("Masukan beda (b) : "))
n = int(input("Jumlah suku (n)  : "))
hasil = deret(a,b,n)
print("Suku ke-",n,"=",hasil)