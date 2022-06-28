a=int(input("masukkan suku awal ="))
b=int(input("masukkan beda ="))
c=int(input("masukkan suku ke="))
for i in range(1, c+1) :
    un = a + (i-1)*b
    print("suku ke -",i,"=",un,"total=",sn)
    sn =(i/2)*(a+un)
print("total=",sn)