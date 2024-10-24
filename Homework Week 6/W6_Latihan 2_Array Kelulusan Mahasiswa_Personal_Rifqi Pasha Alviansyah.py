# Program Kelulusan Mahasiswa, oleh Rifqi Pasha Alviansyah [16424398] 
# Menentukan jumlah mahasiswa yang lulus dan tidak lulus berdasarkan nilai huruf

# KAMUS
# Nilai : array [0..49] of char
# Lulus, TidakLulus : int
# i : int

# ALGORITMA
# Deklarasi array untuk menyimpan nilai 50 mahasiswa
Nilai = [''] * 50  # Inisialisasi array kosong dengan panjang 50 elemen

# Inisialisasi counter lulus dan tidak lulus
Lulus = 0
TidakLulus = 0

# Input nilai dari pengguna untuk setiap mahasiswa
for i in range(50):
    Nilai[i] = input(f"Masukkan nilai huruf untuk mahasiswa ke-{i+1} (A, B, C, D, E): ").upper()

# Proses pengecekan nilai mahasiswa
for i in range(50):
    if Nilai[i] == 'A' or Nilai[i] == 'B' or Nilai[i] == 'C':
        Lulus += 1
    else:
        TidakLulus += 1

# Output jumlah mahasiswa yang lulus dan tidak lulus
print("\nJumlah mahasiswa yang lulus: ", Lulus)
print("Jumlah mahasiswa yang tidak lulus: ", TidakLulus)
