import csv
import datetime

# Menghitung total harga
def hitung_total_harga(jumlah, harga):
    return jumlah * harga

# Mengubah harga menjadi format string yang sesuai dengan mata uang rupiah
def format_harga(harga):
    return f"Rp.{harga:,.0f}"

# Menerima input angka (hanya angka bulat yang valid)
def input_angka(prompt):
    while True:
        try:
            angka = int(input(prompt))
            return angka
        except ValueError:
            print("Input harus berupa angka bulat. Silakan coba lagi.")

# Menerima input item
def input_item(prompt):
    return input(prompt).upper()

# Menerima input nama panggilan CS
def input_cs_name(prompt):
    while True:
        nama_cs = input(prompt)
        if nama_cs.isalpha():
            return nama_cs.upper()
        else:
            print("Format input salah. Masukkan nama panggilan CS menggunakan huruf saja.")

# Membuat ID Transaksi secara otomatis
def buat_id_transaksi(nama_cs):
    tanggal = datetime.date.today().strftime("%y%m%d")
    return f"{nama_cs}-{tanggal}"

# Menyimpan struk belanja ke dalam file CSV
def simpan_struk_ke_csv(nama_file, belanjaan, total_belanja, uang_tunai, kembali):
    with open(nama_file, mode="w", newline="") as file:
        fieldnames = ["Item", "Jumlah", "Harga", "Total Harga"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({"Item": "KEJORA SHOP"})
        writer.writerow({"Item": nama_file})
        writer.writeheader()

        # Tulis header struk
        writer.writerow({"Item": "", "Jumlah": "", "Harga": "", "Total Harga": ""})

        # Tulis setiap item belanja ke dalam file CSV
        for belanja in belanjaan:
            jumlah = belanja["jumlah"]
            item = belanja["item"]
            harga = belanja["harga"]
            total_harga = hitung_total_harga(jumlah, harga)
            writer.writerow({"Item": item, "Jumlah": jumlah, "Harga": format_harga(harga), "Total Harga": format_harga(total_harga)})

        # Tulis total belanja, uang tunai, dan kembalian ke dalam file CSV
        writer.writerow({})
        writer.writerow({"Item": "TOTAL BELANJA", "Jumlah": "", "Harga": "", "Total Harga": format_harga(total_belanja)})
        writer.writerow({"Item": "UANG TUNAI", "Jumlah": "", "Harga": "", "Total Harga": format_harga(uang_tunai)})
        writer.writerow({"Item": "KEMBALIAN", "Jumlah": "", "Harga": "", "Total Harga": format_harga(kembali)})
        writer.writerow({})

        # Tulis footer struk
        writer.writerow({"Item": "TERIMAKASIH DAN SELAMAT BERBELANJA LAGI", "Jumlah": "", "Harga": "", "Total Harga": ""})

# Fungsi untuk melakukan transaksi belanja
def transaksi_belanja():
    belanjaan = []
    total_belanja = 0
    print("Kejora Shop")

    # Input nama panggilan CS
    nama_cs = input_cs_name("Nama panggilan CS: ")

    while True:
        item = input_item('Item (Ketik "0" untuk menyelesaikan transaksi): ')

        if item == "0":
            break

        harga = input_angka("Harga: Rp.")
        jumlah = input_angka("Jumlah: ")

        belanjaan.append({"jumlah": jumlah, "item": item, "harga": harga})

        total_harga = hitung_total_harga(jumlah, harga)
        total_belanja += total_harga

    if belanjaan:
        print("\nStruk Belanja:")
        print("---------------------------")
        for belanja in belanjaan:
            jumlah = belanja["jumlah"]
            item = belanja["item"]
            harga = belanja["harga"]
            total_harga = hitung_total_harga(jumlah, harga)
            print(
                f"{item.upper().ljust(15)}{format_harga(harga).ljust(10)}{str(jumlah).ljust(5)}{format_harga(total_harga)}")
        print("---------------------------")
        print(f"Total Belanja:\t{format_harga(total_belanja)}")

        uang_tunai = input_angka("\nUang Tunai: Rp.")
        kembali = uang_tunai - total_belanja

        print(f"Kembali: {format_harga(kembali)}")

        # Membuat ID Transaksi
        id_transaksi = buat_id_transaksi(nama_cs)

        # Membuat nama file struk
        nama_file = f"{id_transaksi}.csv"

        simpan_struk_ke_csv(nama_file, belanjaan, total_belanja, uang_tunai, kembali)

        print("\nStruk telah disimpan ke dalam file '{nama_file}'.\n")
        print("Terima kasih telah berbelanja di Kejora Shop!")
    else:
        print("Belanjaan kosong. Transaksi dibatalkan.")


if __name__ == '__main__':
    transaksi_belanja()
