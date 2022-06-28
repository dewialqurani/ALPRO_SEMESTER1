a = int(input("masukkan suku awal = "))
b = int(input("masukkan beda = "))
sn = int(input("masukkan nilai total = "))
x=1
y=a
total=y
while total<=sn:
    if y+b <= sn:
        print("suku ke",x,"=",y,"total",total)
    x=x+1
    y=y+b
    total=total+y    
