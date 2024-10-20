## PROGRAM Homework 3 Week 5: Jumlah Genap dan Ganjil, oleh
# Rifqi Pasha Alviansyah    [16424398]
# Alfredo Jumadi Malau      [16424413]
# Muhammad Arif Pratama     [16424389]

"""
Program akan menerima input integer positif dan menampilkan jumlah bilangan genap dan ganjil.
proses dihentikan jika ada bilangan negatif. 0 diasumsikan bilangan genap.
"""

## KAMUS
# N = input bilangan bulat yang akan diperiksa
# jumlah_ganjil = menyatakan jumlah bilangan ganjil dari input
# jumlah_genap = menyatakan jumlah bilangan genap dari input

## ALGORITMA

# INISIALISASI
jumlah_genap = 0
jumlah_ganjil = 0

# AKSI
while True:
    #input bilangan bulat
    N = int(input("Masukan bilangan bulat (masukkan bilangan negatif untuk break): ")) 

    if N < 0:
        break                                           #aksi untuk break ketika input bilangan negatif

    if N % 2 == 0: # N Genap
        jumlah_genap = jumlah_genap + 1                 #jika N mod 2 = 0, maka variabel jumlah_genap bertambah 1

    else: # N Ganjil
        jumlah_ganjil = jumlah_ganjil + 1               #jika N mod 2 != 0, maka variabel jumlah_ganjil bertambah 1

# TERMINASI
print(f"Genap = {jumlah_genap}")
print(f"Ganjil = {jumlah_ganjil}")


