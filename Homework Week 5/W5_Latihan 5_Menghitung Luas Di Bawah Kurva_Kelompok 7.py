## PROGRAM Homework 5 Week 5: Menghitung Luas Di Bawah Kurva, oleh
# Rifqi Pasha Alviansyah    [16424398]
# Alfredo Jumadi Malau      [16424413]
# Muhammad Arif Pratama     [16424389]

"""
Program akan dapat menghitung luas daerah yang dibangun dari rumus f(x) =x^3 + x + 1
dari x=a sampai x=b dengan interval delta, 
dengan a, b, delta merupakan masukan pengguna
"""

## KAMUS
# f(x) = x^3 + x + 1
# a = adalah input (float) batas bawah
# b = adalah input (float) batas atas
# delta = adalah input (float) interval
# total_luas = total luas di bawah kurva dari f(x)
# x_awal = titik awal ; f_x_awal = daerah hasil dari titik awal
# x_akhir = titik akhir ; f_x_akhir = daerah hasil dari titik akhir
# kondisi a<b, b>0, delta>0


#ALGORITMA
# Input batas bawah, batas atas, dan interval delta
a = float(input("Masukkan batas bawah (a, a < b): "))
b = float(input("Masukkan batas atas (b, b > 0): "))
delta = float(input("Masukkan interval delta (delta > 0): "))

# Inisialisasi total luas
total_luas = 0

# Hitung jumlah subinterval
n = int((b - a) / delta)

# Loop untuk menghitung luas setiap trapesium
for i in range(n):
    # Hitung titik awal dan akhir
    x_awal = a + i * delta
    x_akhir = x_awal + delta

    # Hitung f(x) untuk titik awal dan akhir
    f_x_awal = x_awal**3 + x_awal + 1                   # f(x) = x^3 + x + 1
    f_x_akhir = x_akhir**3 + x_akhir + 1                # f(x) = x^3 + x + 1

    # Menghitung luas trapesium dan tambahkan ke total luas
    luas_trapesium = (f_x_awal + f_x_akhir) * delta / 2
    total_luas += luas_trapesium

# Terminasi
print(f"Luas daerah di bawah kurva f(x) dari {a} sampai {b} adalah: {total_luas:.5f}")
