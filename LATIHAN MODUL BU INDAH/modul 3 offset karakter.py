kalimat=input('Masukkan kalimat = ')
huruf=input('Masukkan huruf yang di cari = ')
c=0
for i in range(len(kalimat)) :
    if kalimat[i]==huruf or kalimat.upper()[i]==huruf.upper() :
        c+=1
        print('huruf',huruf,'atau huruf',huruf.upper(),'ke- ',c,': offset- ',i)