def penjumlahan(data) :
    if len(data) == 1 :
        i = penjumlahan(data)
        return i
    else :
        i = sum(data)
        return i
data = [2,3,5,1 ]
hasil = penjumlahan(data)
print ("Jadi total dari  ", data, "=", hasil)