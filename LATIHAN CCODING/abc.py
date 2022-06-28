def total(inisiasi = 5, *num, **key):
    gaskeun = inisiasi
    for n in num:
        gaskeun += n
    for k in key:
        gaskeun += key[k]
    return gaskeun
print(total(5, 250))