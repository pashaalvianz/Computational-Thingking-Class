"""
Tugas Project 1
Mata Kuliah Berpikir Komputasional (WI1102)
Nama Program : " Analisis dan Pengembangan Program Operasional pada Mesin ATM Bersama"
Kelas : 27
Nama Anggota:
    1) Muhammad Arif Pratama (16424389)
    2) Rifqi Pasha Alviansyah (16424398)
    3) Alfredo Jumadi Malau (16424413)
    4) M Zefri Alamsyah (16424415)
    5) Aruna Rodotuah Girsang (16424425)
"""
# Last edited : 6 November 14.00
"""
PENJELASAN PROGRAM/DEKOMPOSISI
1.	Ide Utama 1: Proses Masukkan No Rekening
Sub-poin 1: Tampilkan input untuk No Rekening
1.1	Sub-poin 1.1: Ambil 3 nomor awal dari No Rekening untuk menentukan nama bank.
1.2	Sub-poin 1.2: Cek apakah No Rekening sesuai dengan database.
-	Sub-poin 1.2.1: Apabila No Rekening sesuai, lanjut ke Ide Utama.
-	Sub-poin 1.2.2: Apabila No Rekening tidak sesuai, tampilkan pesan kesalahan dan kembali ke Sub-poin 1.1.

2.	Ide Utama 2: Proses Masukkan PIN.
Sub-poin 2: Tampilkan input untuk memasukkan PIN.
2.1	Sub-poin 2.1: Cek apakah PIN sesuai dengan database
-	Sub-poin 2.1.1: Apabila PIN sesuai, lanjut ke Ide Utama 3
-	Sub-poin 2.1.2: Apabila PIN tidak sesuai:
  -  Sub-poin 2.1.2.1: Tampilkan pesan "PIN salah, masukkan kembali.
  -  Sub-poin 2.1.2.2: Hitung jumlah percobaan
  -  Sub-poin 2.1.2.3: Jika jumlah percobaan kurang dari 3, kembali ke Sub-poin 2. Jika sudah 3 kali dan salah, tampilkan pesan "Transaksi tidak dapat dilanjutkan."

3.	Ide Utama 3: Pilih Menu Transaksi
Sub-poin 3: Tampilkan pilihan menu:
 	1. Tarik Tunai
 	2. Setor Tunai
 	3. Transfer
 	4. Transaksi Lain
 	5. Keluar
4.	Ide Utama 4: Pengecekan Saldo Mengakses Data Saldo Pengguna
4.1	Sub-poin 4.1 : Mengambil data saldo dari sumber data (database). 
4.2	Sub-poin 4.2 : Memproses Data
-	Sub poin 4.2.1 : Apabila saldo tidak dapat ditampilkan, tampilkan pesan "Saldo tidak   dapat ditampilkan saat ini. Silakan coba lagi nanti."
-	Sub-poin 4.2.2 : Apabila Saldo dapat ditampilkan, tampilkan pesan “Saldo anda {Nominal saldo} ”
4.3	Sub-poin 4.3 : Tampilan Saldo (Format Angka dengan Pemisah Ribuan)
-	Sub-poin 4.3.1 :  Mengubah format saldo agar lebih mudah dibaca dengan menggunakan pemisah ribuan (contoh: Rp 5.000.000).
4.4	Sub-poin 4.4 : Tindakan Setelah Pengecekan Saldo 
-	Sub-poin 4.4.1 : Apabila pengguna ingin melanjutkan, tampilkan menu utama untuk   transaksi lain seperti tarik tunai, transfer, dan cek saldo.
-	Sub-poin 4.4.2 : Apabila pengguna memilih keluar, akhiri sesi dengan menampilkan pesan "Terima kasih telah menggunakan layanan kami" lalu akhiri program.

5.	Ide utama 5 : Transaksi Transfer
5.1	Sub-poin 5.1: Transaksi transfer pada bank yang sama
-	Sub-poin 5.1.1: Memilih nomor tujuan transfer
-	Sub-poin 5.1.2: Input nominal transfer yang diinginkan pengguna
-	Sub-poin 5.1.3: Cek apakah saldo pengguna lebih besar atau sama dengan nominal transfer yang diinginkan 
-	Sub-poin 5.1.3.1: Apabila saldo pengguna lebih besar atau sama dengan nominal transfer, bank akan mentransfer sejumlah nominal awal yang di input dan mengurangi saldo dengan nominal yang ditransfer
-	Sub-poin 5.1.3.2: Apabila saldo pengguna lebih kecil dari nominal transfer, transaksi transfer tidak dapat dilakukan, tampilkan pesan "Saldo anda tidak cukup untuk melakukan transaksi transfer
5.2	Sub-poin 1.2: Transaksi transfer pada bank yang berbeda
-	Sub-poin 5.2.1: Memilih nomor tujuan transfer
-	Sub-poin 5.2.2: Input nominal transfer yang diinginkan pengguna
-	Sub-poin 5.2.3: Cek apakah saldo pengguna lebih besar atau sama dengan nominal transfer yang diinginkan serta biaya tambahan (admin)
-	Sub-poin 5.2.3.1: Apabila saldo pengguna lebih besar atau sama dengan nominal transfer serta biaya tambahan (admin), bank akan mentransfer sejumlah nominal awal yang di input dan mengurangi saldo dengan nominal yang ditransfer serta biaya tambahan (admin)
-	Sub-poin 5.2.3.2: Apabila saldo pengguna lebih kecil dari nominal transfer serta biaya tambahan (admin), transaksi transfer tidak dapat dilakukan, tampilkan pesan "Saldo anda tidak cukup untuk melakukan transaksi transfer
 
6.	Ide utama 6: Penarikan tunai
6.1	Sub-poin 6.1: Input nominal yang ingin ditarik
-	Sub-poin 6.1.1: Menerima input nominal uang yang ingin diambil dari saldo rekenging
-	Sub-poin 6.1.2: Apabila nominal yang ingin diambil lebih besar dari saldo rekening, tampilkan pesan “Saldo anda tidak cukup untuk melakukan penarikan tunai” dan hentikan perintah
-	Sub-poin 6.1.3: Berikan opsi untuk penampilan saldo akhir setelah output
6.2	Sub-poin 6.2: Pengolahan input pada saldo rekening
-	Sub-poin 6.2.1: Mengurangi saldo awal pada rekening pengguna dengan input nominal
-	Sub-poin 6.2.2: Mentranslasi input nominal ke uang tunai kertas
6.3	Sub-poin 1.3: Output uang tunai 
-	Sub-poin 6.3.1: Mengeluarkan uang tunai kertas sesuai nilai input nominal
-	Sub-poin 6.3.2: Apabila pengguna memilih “iya” pada pilihan penampilan saldo akhir, tampilkan besar saldo awal setelah dikurangi oleh input nominal
6.4	Sub-poin 6.4: Penentuan pengulangan layanan transaksi
-	Sub-poin 6.4.1 : Apabila pengguna ingin melanjutkan, tampilkan menu utama untuk   	transaksi lain seperti tarik tunai, transfer, dan cek saldo
-	Sub-poin 6.4.2 : Apabila pengguna memilih keluar, akhiri sesi dengan menampilkan pesan                             "Terima kasih telah menggunakan layanan kami" lalu akhiri program.


"""


import time
import pandas as pd
import random

# Data nasabah yang dilayani ATM Bersama hasil generalisasi
nasabah = [
    ["Fufufafa", "1230001", "Bank Mandiri", "1234", 50000000000000000, "081234567890"],
    ["Bayu Eka", "1230002", "Bank Mandiri", "5678", 750000, "081234567891"],
    ["Maria Charissa Paquita", "1230003", "Bank Mandiri", "4321", 300000, "081234567892"],
    ["Charissa Nabilla Rahmadani", "4560001", "Bank BRI", "1111", 2000000, "082345678901"],
    ["Jessie Alvita Maurila", "4560002", "Bank BRI", "2222", 150000, "082345678902"],
    ["Alfian Restu Maulana", "4560003", "Bank BRI", "3333", 6000000, "082345678903"],
    ["Bimo Santoso", "7890001", "Bank BNI", "4444", 800000, "083456789012"],
    ["Dita Amelia Risti", "7890002", "Bank BNI", "5555", 1000, "083456789013"],
    ["Tamara Ayu", "7890003", "Bank BNI", "6666", 9000, "083456789014"],
    ["Joko Widodo", "1230010", "Bank Mandiri", "7777", 4000000000, "081234567895"],
    ["Prabowo Subianto", "4560014", "Bank BRI", "8888", 2500000000000000000, "082345678904"],
    ["Laksita Rachiem", "7890015", "Bank BNI", "9999", 3000000, "083456789015"],
    ["Vanesha Rachell", "1230013", "Bank Mandiri", "1212", 850000, "081234567896"],
    ["Yesa Giventta", "4560016", "Bank BRI", "3434", 720000, "082345678905"],
    ["Muhammad Haikal", "7890017", "Bank BNI", "2323", 18000, "083456789016"],
    ["Hendra Saifullah", "1230018", "Bank Mandiri", "4545", 50000, "081234567897"],
    ["Anissa Rahmawati", "4560019", "Bank BRI", "5656", 350000, "082345678906"],
    ["Gizka Tita Ayu", "7890020", "Bank BNI", "6767", 4000, "083456789017"],
    ["Yohana Ayulellah", "1230021", "Bank Mandiri", "7878", 900000, "081234567898"],
    ["Gregorius Yesaya", "4560022", "Bank BRI", "8989", 500000, "082345678907"],
    ["Ichakkkkk", "7890023", "Bank BNI", "9090", 1000000, "083456789018"],
    ["Zahra", "1230024", "Bank Mandiri", "1010", 6700, "081234567899"],
    ["Erlangga Frizzy", "4560025", "Bank BRI", "1213", 450000, "082345678908"],
    ["Maria Yoppa", "7890026", "Bank BNI", "1414", 11000000, "083456789019"],
    ["Bintang Nuswantara", "1230027", "Bank Mandiri", "1515", 250000, "081234567900"],
    ["Berliandika Fika", "4560028", "Bank BRI", "1616", 800000, "082345678911"],
    ["Agatha Valentina", "7890029", "Bank BNI", "1717", 9500900, "083456789920"],
    ["Valda Hedia", "1230030", "Bank Mandiri", "1818", 1200000, "081234567921"],
    ["Tika Nugraheni", "4560031", "Bank BRI", "1919", 670000, "082345678932"],
    ["Adhwa Almasah", "7890032", "Bank BNI", "2020", 4500000, "083456789034"],
]

# Membuat DataFrame dari data nasabah
nasabah_df = pd.DataFrame(nasabah, columns=["Nama", "NoRekening", "Bank", "PIN", "Saldo", "NoTelepon"])

# Fungsi untuk menghasilkan token listrik 12 digit
def generate_token_listrik():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

# Fungsi untuk validasi input jumlah uang
def validasi_jumlah_uang(jumlah, kelipatan=50000):
    return jumlah > 0 and jumlah % kelipatan == 0

# Tampilan awal ATM sebelum ada user yang menggunakan
print("=== Selamat datang di ATM Bersama ===")
print("=== Layanan ATM Bersama hanya melayani transaksi Bank yang terafiliasi ===")
print("=== Call Centre: (0272) 2177 ===")

time.sleep(3)  # Delay sebelum mulai

# Proses Masukkan No Rekening
akses_diberikan = False
while True:
    norek = input("Silakan Masukkan Kartu Anda: ")
    
    # Identifikasi Jenis Bank berdasarkan 3 digit pertama nomor rekening
    if norek.startswith("123"):
        bank_teridentifikasi = "Bank Mandiri"
    elif norek.startswith("456"):
        bank_teridentifikasi = "Bank BRI"
    elif norek.startswith("789"):
        bank_teridentifikasi = "Bank BNI"
    else:
        print("Bank tidak dikenal, silakan masukkan Kartu ATM Bank yang Terafiliasi.")
        continue

    # Cek apakah No Rekening sesuai dengan database
    if norek in nasabah_df["NoRekening"].values:
        user = nasabah_df[nasabah_df["NoRekening"] == norek]
        break
    else:
        print("Nomor rekening tidak dikenali. Silakan coba nomor rekening yang lain.")
        time.sleep(5)
        
# Proses Masukkan PIN
while not akses_diberikan:
    pin = input("Masukkan PIN Anda: ")
    if pin == user["PIN"].values[0]:
        akses_diberikan = True
        nama_user = user["Nama"].values[0]
        print(f"Selamat datang, {nama_user} dari {bank_teridentifikasi}.")
        time.sleep(3)
    else:
        print("PIN salah, masukkan kembali.")
        time.sleep(3)

# Menu utama
selesai = False
while not selesai:
    print("\nPilih Menu Transaksi:")
    print("1. Tarik Tunai")
    print("2. Setor Tunai")
    print("3. Transfer")
    print("4. Transaksi Lainnya")
    print("5. Keluar")
    time.sleep(3)

    pilihan = input("Masukkan pilihan Anda: ") # pengguna menginput pilihan

    if pilihan == "1":  # Tarik Tunai
        while True:
            jumlah_tarik = int(input("Masukkan jumlah uang yang ingin ditarik (kelipatan 50.000): "))
            if not validasi_jumlah_uang(jumlah_tarik):
                print("Jumlah tidak valid, harus positif dan kelipatan 50.000.")
                continue
            elif jumlah_tarik > user["Saldo"].values[0]:
                print("Saldo tidak mencukupi.")
                continue

            nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"] -= jumlah_tarik
            print(f"Anda telah berhasil menarik tunai sebesar Rp {jumlah_tarik}")
            time.sleep(1)
            tampilkan_saldo = input("Apakah Anda ingin menampilkan saldo akhir? (y/n): ").lower()
            if tampilkan_saldo == 'y':
                saldo_akhir = nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"].values[0]
                print(f"Sisa saldo Anda: Rp {saldo_akhir}")
            break

    elif pilihan == "2":  # Setor Tunai
        while True:
            jumlah_setor = int(input("Masukkan jumlah uang yang ingin disetor (kelipatan 50.000): "))
            if not validasi_jumlah_uang(jumlah_setor):
                print("Jumlah tidak valid, harus positif dan kelipatan 50.000.")
                continue

            nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"] += jumlah_setor
            print(f"Anda telah berhasil menyetor sebesar Rp {jumlah_setor}")
            tampilkan_saldo = input("Apakah Anda ingin menampilkan saldo akhir? (y/n): ").lower()
            if tampilkan_saldo == 'y':
                saldo_akhir = nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"].values[0]
                print(f"Sisa saldo Anda: Rp {saldo_akhir}")
            break
            break


    elif pilihan == "3": # Transfer
        norek_tujuan = input("Masukkan nomor rekening tujuan: ")
        jumlah_transfer = int(input("Masukkan jumlah transfer: "))
        user_tujuan = nasabah_df[nasabah_df["NoRekening"] == norek_tujuan]
        if not user_tujuan.empty:
            konfirmasi = input(f"Apakah Anda yakin ingin mentransfer Rp {jumlah_transfer} ke nomer rekening rekening atas nama {user_tujuan['Nama'].values[0]}? (y/n): ").lower()
            if konfirmasi == 'y':
                if jumlah_transfer <= user["Saldo"].values[0]:
                    nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"] -= jumlah_transfer
                    nasabah_df.loc[nasabah_df["NoRekening"] == norek_tujuan, "Saldo"] += jumlah_transfer
                    print(f"Transfer sebesar Rp {jumlah_transfer} berhasil.")
                else:
                    print("Saldo tidak mencukupi.")
            else:
                print("Transfer dibatalkan.")
            
        else:
            print("Rekening tujuan tidak ditemukan.")

    elif pilihan == "4":  # Transaksi Lainnya
        print("\nTransaksi Lainnya:")
        print("1. Cek Saldo")
        print("2. Call Centre")
        print("3. Pembelian Pulsa")
        print("4. Pembayaran Listrik")
        print("5. Pembayaran Air")
        print("6. Pembayaran BPJS")
        transaksi_lain = input("Masukkan pilihan Anda: ")

        if transaksi_lain == "1":  # Cek Saldo
            saldo = nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"].values[0]
            print(f"Sisa saldo Anda: Rp {saldo}")
            time.sleep(1)
        
        elif transaksi_lain == "2":  # Call Centre
            print("Anda dapat menghubungi")
            time.sleep(2)
            print("Telp. (0272) 2177 atau WA. 08177923996")
        
        elif transaksi_lain == "3":  # Pembelian Pulsa
            no_hp = input("Masukkan nomor HP yang ingin dibeli pulsa: ")
            jumlah_pulsa = int(input("Masukkan nominal pulsa: "))
            konfirmasi = input(f"Apakah Anda yakin ingin membeli pulsa Rp {jumlah_pulsa} untuk nomor {no_hp}? (y/n): ").lower()
            if konfirmasi == 'y':
                if jumlah_pulsa > user["Saldo"].values[0]:
                    print("Saldo tidak mencukupi.")
                else:
                    nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"] -= jumlah_pulsa
                    print(f"Pembelian pulsa sebesar Rp {jumlah_pulsa} untuk nomor {no_hp} berhasil.")
            else:
                print("Pembelian pulsa dibatalkan.")

        elif transaksi_lain == "4":  # Pembayaran Listrik
            id_pelanggan = input("Masukkan ID Pelanggan listrik: ")
            kode_bayar = input("Masukkan kode pembayaran listrik: ")
            jumlah_pembayaran = int(input("Masukkan jumlah pembayaran: "))
            konfirmasi = input(f"Apakah Anda yakin ingin membayar Rp {jumlah_pembayaran} untuk ID Pelanggan {id_pelanggan} di PT. PLN Persero? (y/n): ").lower()
            if konfirmasi == 'y':
                if jumlah_pembayaran > user["Saldo"].values[0]:
                    print("Saldo tidak mencukupi.")
                else:
                    nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"] -= jumlah_pembayaran
                    token_listrik = generate_token_listrik()
                    print(f"Pembayaran listrik berhasil sebesar Rp {jumlah_pembayaran}. Kode token listrik Anda: {token_listrik}")
            else:
                print("Pembayaran listrik dibatalkan.")

        elif transaksi_lain == "5":  # Pembayaran Air
            id_air = input("Masukkan ID Pelanggan air: ")
            kode_bayar = input("Masukkan kode pembayaran air: ")
            jumlah_pembayaran = int(input("Masukkan jumlah pembayaran: "))
            konfirmasi = input(f"Apakah Anda yakin ingin membayar Rp {jumlah_pembayaran} untuk ID Pelanggan {id_air} di PT. Tirta Merapi? (y/n): ").lower()
            if konfirmasi == 'y':
                if jumlah_pembayaran > user["Saldo"].values[0]:
                    print("Saldo tidak mencukupi.")
                else:
                    nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"] -= jumlah_pembayaran
                    print(f"Pembayaran air ke PT. Tirta Merapi berhasil sebesar Rp {jumlah_pembayaran}.")
            else:
                print("Pembayaran air dibatalkan.")

        elif transaksi_lain == "6":  # Pembayaran BPJS
            id_bpjs = input("Masukkan No Kepesertaan BPJS: ")
            kode_bayar = input("Masukkan kode pembayaran BPJS: ")
            jumlah_pembayaran = int(input("Masukkan jumlah pembayaran: "))
            konfirmasi = input(f"Apakah Anda yakin ingin membayar Rp {jumlah_pembayaran} untuk BPJS ke PT. Jasa Raharja Kesehatan? (y/n): ").lower()
            if konfirmasi == 'y':
                if jumlah_pembayaran > user["Saldo"].values[0]:
                    print("Saldo tidak mencukupi.")
                else:
                    nasabah_df.loc[nasabah_df["NoRekening"] == norek, "Saldo"] -= jumlah_pembayaran
                    print(f"Pembayaran BPJS ke PT. Jasa Raharja Kesehatan berhasil sebesar Rp {jumlah_pembayaran}.")
            else:
                print("Pembayaran BPJS dibatalkan.")

    elif pilihan == "5":  # Keluar
        print("Apakah Anda yakin ingin melakukan keluar? (y/n): ", end="")
        transaksi_lain = input().lower()
        if transaksi_lain == 'n':
            continue
        else:
            print("Terima kasih telah menggunakan ATM Bersama. Silakan ambil kartu Anda.")
            selesai = True

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
