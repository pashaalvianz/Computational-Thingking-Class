#PROGRAM LATIHAN 1: MENGHITUNG JARAK
# program harus dapat menghitung jarak (dalam meter) yang ditempuh berdasarkan masukan kecepatan dalam (meter per sekon) dan waktu (dalam sekon)

#KAMUS
# v = kecepatan, dalam meter per sekon (m/s)
# t = waktu tempuh, dalam sekon (s)
# j = jarak tempuh, dalam meter (m)

#ALGORITMA
# input
v = float(input("Masukan kecepatan (m/s):"))
t = float(input("Masukan waktu tempuh (s): "))

# validasi (karena kecepatan/speed dan waktu/time tidak mungkin bilangan tak-positif, maka harus dibuat validasi v, t >= 0)
while v < 0:
    print("Kecepatan tidak boleh negatif. Silakan masukan nilai yang valid")
    v = float(input("Masukan kecepatan (m/s): "))
while t < 0:
    print("Waktu tempuh tidak boleh negatif. Silakan masukan nilai yang valid")
    t = float(input("Masukan waktu tempuh (s): "))

# proses (menghitung jarak menggunakan hukum fisika)
j = v * t

# output
print(f"Jarak yang ditempuh adalah {j} meter")