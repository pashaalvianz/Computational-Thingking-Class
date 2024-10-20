## PROGRAM Homework 4 Week 5: [VERSI WHILE] Lagu Anak Ayam, oleh
# Rifqi Pasha Alviansyah    [16424398]
# Alfredo Jumadi Malau      [16424413]
# Muhammad Arif Pratama     [16424389]

"""
[VERSI WHILE] Program akan menerima masukan jumlah anak ayam, lalu 
menuliskan lagu anak ayam berdasarkan jumlah anak ayam tersebut menggunakan looping while
"""

## KAMUS
# N = input (int) jumlah anak ayam

## ALGORITMA

# input (asumsi N>0, tidak perlu dicek)
N = int(input("Masukkan jumlah anak ayam: "))
# menampilkan bait pertama lagu
print(f"Anak ayam turunlah {N}")

# aksi 
i = N-1                                         
while (i >= 1):                                 # mencegah n<1 untuk masuk ke looping
    print(f"Mati satu tinggallah {i} ")             
    i-=1                                        # melooping dengan jumlah anak ayam yang berkurang 1

# terminasi
print("Mati satu tinggal induknya")             


"""
[KESIMPULAN] Penggunaan while lebih tepat karena lebih aman dan fleksibel dalam menangani kondisi N = 1.
Dalam versi while, kondisi pengulangan langsung ditangani di awal dengan while N > 1. 
Ini memastikan bahwa jika N = 1, program tidak akan memasuki loop, 
dan langsung melanjutkan ke bagian akhir yang mencetak "Mati satu tinggal induknya."
"""