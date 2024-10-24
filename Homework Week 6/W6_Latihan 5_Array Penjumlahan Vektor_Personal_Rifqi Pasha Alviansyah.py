# Program Penjumlahan Dua Vektor, oleh Rifqi Pasha Alviansyah [16424398]
# Menjumlahkan dua vektor V dan U yang masing-masing terdiri atas 5 elemen

# KAMUS
# V, U, W : array [0..4] of int
# i : int (indeks)

# ALGORITMA
# Deklarasi dan input nilai vektor V
V = [int(input(f"Masukkan elemen V{i}: ")) for i in range(5)]

# Deklarasi dan input nilai vektor U
U = [int(input(f"Masukkan elemen U{i}: ")) for i in range(5)]

# Inisialisasi vektor W untuk menyimpan hasil penjumlahan
W = [0] * 5

# Penjumlahan elemen-elemen dari vektor V dan U
for i in range(5):
    W[i] = V[i] + U[i]

# Cetak hasil penjumlahan vektor W
print("Hasil penjumlahan kedua vektor W adalah:", W)
