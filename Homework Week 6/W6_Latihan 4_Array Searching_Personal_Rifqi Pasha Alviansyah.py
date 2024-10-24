# Program SearchArray, oleh Rifqi Pasha Alviansyah [16424398]
# Mencari indeks pertama di mana X ditemukan di T

# KAMUS
# N : int (ukuran array)
# T : array [0..N-1] of int
# i, X : int
# found : bool (menentukan apakah X sudah ditemukan)

# ALGORITMA
# Input jumlah elemen dalam array
N = int(input("Masukkan jumlah elemen N: "))

# Deklarasi array T dan input nilainya
T = [int(input(f"Masukkan elemen ke-{i+1}: ")) for i in range(N)]

# Input nilai X yang dicari
X = int(input("Masukkan nilai X yang dicari: "))

# Inisialisasi variabel
found = False  # X belum ditemukan
i = 0  # Inisialisasi indeks

# Pencarian nilai X
while (i < N and not found):
    if T[i] == X:
        found = True  # X ditemukan
    else:
        i += 1  # Increment jika X belum ditemukan

# Cetak hasil pencarian
if found:
    print(f"Nilai {X} ditemukan di indeks ke-{i}")
else:
    print(f"Nilai {X} tidak ditemukan di array T")
