#Bilangan Eksponen Iteratif
def eksponen_iteratif(x,n):
    if (n == 0):
        for i in range(n+1):
            return(1)
    else:
        for i in range(n+1):
            hasil = x ** (i)
            print(x,"^",i,"=",hasil)
            i += 1
    return(hasil)

#Bilangan Eksponen Recursive
def eksponen_recursive(x,n):
    if (n == 0):
        return(1)
    else:
        return(x * eksponen_recursive(x,n-1))
x = int(input("Masukan angka : "))
n = int(input("Masukan pangkat(n) : "))
print("Eksponen Iteratif")
eksponen_iteratif(x,n)
print("Eksponen Recursive")
k = eksponen_recursive(x,n)
print(k)