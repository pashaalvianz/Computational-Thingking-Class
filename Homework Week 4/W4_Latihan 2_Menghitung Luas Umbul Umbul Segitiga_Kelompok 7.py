#PROGRAM Latihan 2: Menghitung Luas Umbul-Umbul Segitiga
# program harus dapat menghitung luas umbul-umbul segitiga berdasarkan masukan tinggi dan alas
# masih belum ditentukan masukan tinggi dan alas dalam satuan apa, maka akan disepakati bahwa program menggunakan masukan dalam satuan meter

#KAMUS
# t = tinggi segitiga, dalam satuan meter
# a = alas segitiga, dalam satuan meter
# L = luas umbul-umbul segitiga, dalam satuan meter persegi ----> Rumus: L = 0.5 * a * t


#ALGORITMA

# input 
t = float(input("Masukan nilai tinggi segitiga dalam meter: "))
a = float(input("Masukan nilai alas segitiga dalam satuan meter: "))

# validasi (karena tinggi dan alas tidak mungkin nilai tak-positif, maka harus dibuat validasi tinggi dan alas >= 0)
while t < 0:
    print("Tinggi segitiga tidak boleh negatif. Silakan masukan nilai yang valid")
    t = float(input("Masukan nilai tinggi segitiga dalam meter: "))
while a < 0:
    print("Alas segitiga tidak boleh negatif. Silakan masukan nilai yang valid")
    a = float(input("Masukan nilai alas segitiga dalam satuan meter:"))

# proses (menghitung luas umbul-umbul)
L = 0.5 * a * t

# output
print(f"Luas umbul-umbul segitiga adalah {L} meter persegi")
