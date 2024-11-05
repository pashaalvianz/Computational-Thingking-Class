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
"""


"""


import time
import pandas as pd
import random

# Data nasabah yang dilayani ATM Bersama hasil generalisasi
nasabah = [
    ["Albrian Wijaya", "1230001", "Bank Mandiri", "1234", 500000000, "081234567890"],
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
