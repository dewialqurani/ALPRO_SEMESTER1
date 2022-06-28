data=input('Masukkan kalimat anda ')
a=input('Masukkan huruf yang dicari ')
temp=0
for i in range(len(data)):
    if data.upper()[i]==a.upper() or data[i]==a:
        temp+=1
        print('huruf', data.upper()[i], 'ke', temp,'=',i)

