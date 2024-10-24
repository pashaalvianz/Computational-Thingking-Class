# Program Pencarian Nilai Ekstrem (Minimum), oleh Rifqi Pasha Alviansyah [16424398]
# Mencari nilai terkecil dari elemen array

# KAMUS
# N : int (jumlah elemen dalam array)
# T : array [0..N-1] of int
# i : int
# min : int

# ALGORITMA
# Input jumlah elemen dalam array
N = int(input("Masukkan jumlah elemen N: "))

# Deklarasi array T dan input nilainya
T = [int(input(f"Masukkan elemen ke-{i+1}: ")) for i in range(N)]

# Inisialisasi nilai minimum dengan elemen pertama
min = T[0]

# Pencarian nilai minimum dimulai dari elemen kedua
for i in range(1, N):
    if T[i] < min:
        min = T[i]

# Cetak nilai terkecil
print("Nilai terkecil =", min)
