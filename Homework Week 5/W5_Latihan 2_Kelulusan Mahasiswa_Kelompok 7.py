## PROGRAM Homework 2 Week 5: Kelulusan Mahasiswa, oleh
# Rifqi Pasha Alviansyah    [16424398]
# Alfredo Jumadi Malau      [16424413]
# Muhammad Arif Pratama     [16424389]

"""
Program akan menerima input banyak mahasiswa dan indeks nilai tiap mahasiswa. 
setelah diklasifikasi nilainya terhadap kelulusan mahasiswa, program menampilkan jumlah lulus dan tidak lulus 
"""

## KAMUS
# N = input jumlah mahasiswa di kelas
# lulus = jumlah mahasiswa yang dinyatakan lulus
# tidak_lulus = jumlah mahasiswa yang dinyatakan tidak lulus

## ALGORITMA

# input (asumsi N>0, tidak perlu diperiksa)
N = int(input("Masukkan jumlah mahasiswa di kelas: "))

# INISIALISASI
lulus = 0
tidak_lulus = 0

# AKSI
for i in range(N):
    # input nilai mahasiswa ke-i
    nilai = input(f"Masukkan nilai mahasiswa ke-{1+i}: ")
    # aksi, memeriksa mahasiswa apakah lulus atau tidak
    if nilai in ['A', 'B', 'C', 'D']: 
        lulus = lulus + 1                   # jika lulus, jumlah variabel lulus akan bertambah 1
    else: #nilai E atau F
        tidak_lulus = tidak_lulus + 1       # jika tidak lulus, jumlah variabel tidak_lulus akan bertambah 1

# TERMINASI
print(f"Lulus = {lulus}")
print(f"Tidak lulus = {tidak_lulus}")