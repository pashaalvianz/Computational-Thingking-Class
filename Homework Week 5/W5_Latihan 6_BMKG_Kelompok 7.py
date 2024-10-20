## PROGRAM Homework 5: Menghitung Statistik Suhu Udara di Kota Bandung, oleh  
# Rifqi Pasha Alviansyah    [16424398]  
# Alfredo Jumadi Malau      [16424413]  
# Muhammad Arif Pratama     [16424389]  

"""
Program akan menghitung suhu rata-rata, suhu tertinggi, dan suhu terendah 
dari suhu udara di Kota Bandung selama N hari (28, 29, 30, atau 31), 
dengan N merupakan masukan pengguna.
"""

# ALGORITMA
# Input jumlah hari dalam sebulan
N = int(input("Masukkan jumlah hari dalam sebulan (ex. 28, 29, 30, atau 31): "))

# Inisialisasi variabel untuk menghitung suhu
total_suhu = 0
suhu_tertinggi = float('-inf')  # Set suhu tertinggi awal ke nilai terendah
suhu_terendah = float('inf')     # Set suhu terendah awal ke nilai tertinggi

# Input suhu harian
for i in range(1, N + 1):
    suhu_harian = float(input(f"Masukkan suhu hari ke-{i}: "))
    
    # Hitung total suhu
    total_suhu += suhu_harian
    
    # Cek suhu tertinggi
    if suhu_harian > suhu_tertinggi:
        suhu_tertinggi = suhu_harian
    
    # Cek suhu terendah
    if suhu_harian < suhu_terendah:
        suhu_terendah = suhu_harian

# Hitung suhu rata-rata
suhu_rata_rata = total_suhu / N

# Output hasil
print(f"Suhu rata-rata selama {N} hari: {suhu_rata_rata:.2f} °C")
print(f"Suhu tertinggi: {suhu_tertinggi:.2f} °C")
print(f"Suhu terendah: {suhu_terendah:.2f} °C") 
