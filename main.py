print("       SELAMAT DATANG DI TOKO VEBYMART        ") 
print("      TOKO GROSIR PALING LENGKAP     ")

#inputan
nama_barang = input(" nama barang : ")
harga_barang = int(input(" harga barang : "))
jumlah_barang = int(input(" jumlah barang : "))
    
total = harga_barang * jumlah_barang
print("jadi semuanya RP.",total) 
pembayaran = int(input("masukan pembayaran : "))
kembalian = pembayaran - total

status_pembayaran = print('Pembayaran Berhasil,',"  ini kembalian nya RP.", kembalian,",   TERIMA KASIH ATAS KUNJUNGAN NYA" ) if (pembayaran >= total) else print('Uang Anda Kurang')


