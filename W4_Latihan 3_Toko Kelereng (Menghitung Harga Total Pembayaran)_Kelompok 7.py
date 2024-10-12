#PROGRAM Latihan 3: Toko Kelereng (Menghitung Total Pembayaran)
# program harus dapat menghitung total pembayaran berdasarkan jumlah kelereng merah, hijau, dan kuning yang dibeli oleh seorang anak

#KAMUS
# m = jumlah kelereng merah
# h = jumlah kelereng hijau
# k = jumlah kelereng kuning
# harga_merah = harga 1 butir kelereng merah dalam rupiah
# harga_hijau = harga 1 butir kelereng hijau dalam rupiah
# harga_kuning = harga 1 butir kelereng kuning dalam rupiah
# harga_total = harga total pembayaran yang harus di bayarkan seorang adik dalam rupiah
# Rumus: harga_total = (harga_merah * m) + (harga_hijau * h) + (harga_kuning * k)

#ALGORITMA

# input
m = int(input("Masukan jumlah kelereng merah: "))
h = int(input("Masukan jumlah kelereng hijau: "))
k = int(input("Masukan jumlah kelereng kuning: "))

# proses harga per jenis kelereng
harga_merah = 10 * 100            #harga dalam rupiah
harga_hijau = 15 * 100            #harga dalam rupiah
harga_kuning = 20 * 200           #harga dalam rupiah

# proses total harga pembayaran
harga_total = (harga_merah * m) + (harga_hijau * h) + (harga_kuning * k)

# output
print(f"Harga total yang harus dibayarkan adalah {harga_total} rupiah")
