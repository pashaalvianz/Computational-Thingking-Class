## PROGRAM Homework 4 Week 5: [VERSI FOR] Lagu Anak Ayam, oleh
# Rifqi Pasha Alviansyah    [16424398]
# Alfredo Jumadi Malau      [16424413]
# Muhammad Arif Pratama     [16424389]

"""
[VERSI FOR] Program akan menerima masukan jumlah anak ayam, lalu 
menuliskan lagu anak ayam berdasarkan jumlah anak ayam tersebut menggunakan looping for
"""

## KAMUS
# N = input (int) jumlah anak ayam

## ALGORITMA

# input (asumsi N>0, tidak perlu dicek)
N = int(input("Masukkan jumlah anak ayam: "))
# menampilkan bait pertama lagu
print(f"Anak ayam turunlah {N}")

# aksi 
if N > 1:                                       
    for i in range (N-1, 0, -1):
        print(f"Mati satu tinggallah {i}")      # memuat aksi untuk looping menuliskan bait mati satu tinggallah N-1 dst.

# terminasi
print("Mati satu tinggal induknya")             # menampilkan bait terakhir lagu

"""
[KESIMPULAN] penggunaan looping menggunakan "for" kurang tepat, karena looping untuk N = 1 akan bermasalah.
Jika N = 1, kasus kosong terjadi karena pengulangan tidak masuk ke loop sama sekali. 
Untuk mencegah hal ini, digunakan kondisi if-else. Jadi kurang efisien dan fleksibel.
"""