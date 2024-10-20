## Program Homework 1 Week 5: Penjumlahan Kelipatan 5 Suatu Integer, oleh
# Rifqi Pasha Alviansyah    [16424398]
# Alfredo Jumadi Malau      [16424413]
# Muhammad Arif Pratama     [16424389]

"""
Program akan menerima masukan integer positif, misal N, lalu akan
menampilkan penjumlahan semua bilangan keipatan 5 antara 1 s.d N
"""

## KAMUS
# N = input bilangan integer positif
# jumlah_n = Jumlah semua bilangan kelipatan 5 antara 1 s.d N

## ALGORITMA

## memeriksa input apakah integer positif
while True:
    # masukkan nilai n
    N = int(input("Masukkan bilangan bulat positif: "))
    # validasi
    if N > 0:
        break # jika valid, maka keluar dari looping
    else: 
        print("Nilai harus bilangan bulat positif. Silakan coba lagi") # jika tidak valid, meminta pengguna memasukan ulang input dan kembali ke looping

# Inisialisasi
jumlah_n = 0

# Menghitung penjumlahan bilangan kelipatan 5
for i in range (1, N+1):          
    if i % 5 == 0:
        jumlah_n += i

# Terminasi
print(jumlah_n)