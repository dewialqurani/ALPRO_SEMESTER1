a = int(input("MASUKKAN ANGKA => "))
if a>1:
    for i in range(2,a-1+1,1):
        if a % i == 0:
            print("bukan prima")
            break
    else:
        print("prima")
else:
    print("bukan prima")                      
        
