print('SELAMAT DATANG DI BANK D.I.A')
print('============================================')
pilihan = ('Ya')
peluang = 3
saldo = 500000
while peluang >= 0:
    pin =int(input('Silahkan Masukkan 6 Digit PIN Anda :  '))
    print('============================================')
    if pin == (188199):
        print('PIN yang Anda Masukkan Benar\n')
        while pilihan not in ('Tidak'):
            print('\nSilahkan pilih 1 untuk informasi saldo')
            print('Silahkan pilih 2 penarikan tunai')
            print('Silahkan pilih 3 pembayaran')
            print('Silahkan pilih 4 keluar')
            print('')
            pilih = int(input('Pilih Transaksi yang Anda Inginkan : '))
            print('============================================')

            if pilih == 1:
                print('Saldo Rekening Anda Rp. ', saldo, '\n')
                print('============================================')
                pilihan = input('Anda ingin Melakukan Transaksi lain ? ')
                if pilihan in ('Tidak'):
                    print('Terimakasih')
                    break
                
            elif pilih == 2:
                if saldo < 100000 :
                    print('Maaf, Saldo Anda Tidak Mencukupi ')
                    print('============================================')
                    print('Silahkan Isi Saldo Anda Terlebih Dahulu')
                else : 
                    print('Silahkan Pilih Jumlah Penarikan \nRp.100.000\nRp.300.000\nRp.500.000\nRp.1.000.000\nRp.2.500.000\n ')
                    tarik = int(input('Masukkan Nominal Penarikan Anda : '))
                    if (tarik == 100000) or (tarik == 300000) or (tarik == 500000) or (tarik == 1000000) or (tarik == 2500000) :
                        saldo = saldo - tarik
                        print('Nominal yang Anda Tarik Rp. ', tarik)
                        print('============================================')
                        print('Sisa Saldo Anda sekarang Rp. ', saldo)
                        print('============================================')
                        pilihan = input('Anda ingin Melakukan Transaksi lain ? ')
                        if pilihan in ('Tidak'):
                            print('Terimakasih')
                            break
                    else :
                        print('\nNominal Yang Anda Masukkan Tidak Diketahui')

            elif pilih == 3:
                bayar = int(input('Berapa Jumlah yang ingin Anda Bayar ? '))
                saldo = saldo + bayar
                print('\nSaldo Anda Sekarang Rp.  ', saldo)
                print('============================================')
                pilihan = input('Apakah Anda ingin  Kembali ? ')
                if pilihan in ('Tidak'):
                    print('Terimakasih')
                    break

            elif pilih == 4:
                print('Harap Tunggu  ... \n')
                print('============================================')
                print('Terimakasih Telah Mempercayai Kami')
                break

            else:
                print('Harap Masukkan Nomor Yang Benar : \n')
                pilihan = ('Ya')

    elif pin != (188199):
        print('PIN yang Anda Masukkan Salah\n')
        peluang = peluang - 1
        if peluang == 0:
            print('\nMaaf Rekening Anda Kami Tangguhkan selama 24 Jam ')
            break