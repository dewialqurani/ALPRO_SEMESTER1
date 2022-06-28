print("\n*------------ D.I.A STORE ------------*\n")
barang =[
        ["SPIRULINA" , "5.000"],
        ["VITALINE" , "15.000"],
        ["ZINC" , "4.000"],
        ["TEH" , "5.000"],
        ["FACE WASH" , "30.000"],
        ["NONITREND" , "3.500"],
]

print("-"*47,"\n")
print("|"," "*14,"STOK PRODUK"," "*16,"|","\n")
print("-"*47)
print("|","No".center(7),"|","BARANG".center(15),"|","HARGA".center(15),"|")
for i in range(1,len(barang)+1):
    barang1 = barang[i-1][0]
    barang2 = barang[i-1][1]  
    for z in range(1):
        print("-"*47)
        print("|","".center(2),i,"".center(2),"|",barang1.center(15),"|",barang2.center(15),"|")
print("-"*47)

nama_barang = input("Nama Barang : ")  

if nama_barang=="SPIRULINA":
    harga = 5.000
elif nama_barang=="VITALINE":
    harga = 15.000
elif nama_barang=="ZINC":
    harga = 4.000
elif nama_barang=="TEH":
    harga = 5.000
elif nama_barang=="FACE WASH":
    harga = 30.000
elif nama_barang=="NONITREND":
    harga = 3.500
else:
    while True:
        print("======Menu Tidak Tersedia, Silahkan Pilih Menu Lainnya!======")
        nama_barang = input("Nama Barang : ") 
        if nama_barang=="SPIRULINA":
            harga = 5.000
        elif nama_barang=="VITALINE":
            harga = 15.000
        elif nama_barang=="ZINC":
            harga = 4.000
        elif nama_barang=="TEH":
            harga = 5.000
        elif nama_barang=="FACE WASH":
            harga = 30.000
        elif nama_barang=="NONITREND":
            harga = 3.500
        else:
            print("INVALID")

jumlah_pembelian = int(input("Jumlah pembelian : "))
Harga_Satuan = int(input("Harga Satuan : "))


print("-"*83)
print(" ".center(30),"WIDANG 08585140365 ".center(15))
print(" "*(25),"JL. PATRIOT WIDANG TUBAN 62383".center(15))
print(" "*(30),"STRUK PEMBAYARAN".center(15))
import time;

localtime = time.asctime( time.localtime(time.time()) )
print (localtime)

print("-"*83)
print("|","No".center(7),"|","NAMA BARANG".center(15),"|","JUMLAH".center(15),"|","HARGA SATUAN".center(15),"|","SUB TOTAL".center(15),"|")
print("-"*83)
print("|","1".center(7),"|",nama_barang.center(15),"|",str(jumlah_pembelian).center(15),"|", str(Harga_Satuan).center(15),"|",str(Harga_Satuan*jumlah_pembelian).center(15),"|")
print("-"*83)

Total1 = (jumlah_pembelian*Harga_Satuan)
if Total1 > 100000:
    print("Diskon   :   2%")
    Diskon = 0.02*Total1
    Total =  (Total1-Diskon)


else: 
    print("Diskon : 0")
    Total = Total1
Harga_total = Total
print("Total    :   Rp. ",Harga_total)

def pembayaran():
    Bayar1 = int(input("Bayar    :   Rp.  "))
    if Bayar1 > Harga_total:
        Kembalian = print("Kembali  :   Rp. ",Bayar1 - Total)

    elif Bayar1 ==Harga_total:
        print("Uang Anda Pas")

    else:
        print("Maaf, pembayaran anda kurang dari total transaksi sebesar Rp. ",Harga_total)
        print("Mohon lakukan transaksi ulang")
        pembayaran()

pembayaran()



print("~~~~~~~~~~TERIMAKASIH SUDAH BERBELANJA~~~~~~~~~~\n")
print("                  Nb : Barang yang sudah dibeli tidak bisa dikembalikan")