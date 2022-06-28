def aritmatika(data):
    if len(data)==1:
        return data[0]
    else:
        x = aritmatika(data[1:])
        return data [0]+x

angka = [2,4,6,8]
print('deret',angka)
print('hasil',aritmatika(angka))