n = int(input('masukkan nilai n = '))
y=0

for i in range(n):
    rumus = 4*(i+1)+5
    y+=rumus
    print('4*', i+1 ,'+5', rumus)
print('sigma = ',y)    