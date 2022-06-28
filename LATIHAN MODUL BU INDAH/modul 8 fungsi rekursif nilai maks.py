def Maksimal(data) :
    if len(data) == 1 :
        i = Maksimal(data)
        return i
    else :
        i = max(data)
        return i
data = [ 15, 11, 10 ]
hasil = Maksimal(data)
print ("Max number :  ", data, "=", hasil)