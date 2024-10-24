# Program Array Scaling, oleh Rifqi Pasha Alviansyah [16424398]
# Mengalikan seluruh elemen array dengan sebuah integer

# KAMUS
# T : array [0..19] of int
# X : pengali array T (int)
# i : int

# ALGORITMA
# Deklarasi array dengan value untuk seluruh elemen
T = [4, 1, 3, 4, 5, 6, 8, 9, 12, 30, -1, 0, 4, -1, -3, 10, 14, 6, 7, 0]

# Input X pembacaan nilai dari keyboard
X = int(input("Masukkan nilai X untuk mengalikan semua elemen array T: "))

# Menghitung nilai perkalian semua elemen array T dengan x dan menampilkan hasilnya ke layar
for i in range(0,20):
    print(T[i] * X)