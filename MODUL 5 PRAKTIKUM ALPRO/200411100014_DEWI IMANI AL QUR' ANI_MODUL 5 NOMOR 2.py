pembagi = []
def faktor(x):
        for i in range(1, x+1):
            if x%i ==0:
                pembagi.append(i)
        return pembagi
num = int(input('Masukkan angka = '))
print('Bilangan Pembagi = ', faktor(num))










