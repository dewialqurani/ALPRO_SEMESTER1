data=int(input('masukkan nilai  = '))
nilai=data%5
if data > 40:
    if data % 5 <3 :
        if nilai == 0:
            data=data
        elif nilai==1:
            data=data-1
        else :
            data=data-2
    else :
        if nilai == 3:
            data=data + 2
        else :
            data=data + 1
else :
    data=data
print('pembulatan = ',data)