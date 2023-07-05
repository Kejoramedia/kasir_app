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

# Menerima input counter untuk ID transaksi
def input_counter(prompt):
    while True:
        counter = input(prompt)
        if counter.isdigit() and len(counter) == 3:
            return int(counter)
        else:
            print("Input harus dalam bentuk angka 3 digit. Silakan coba lagi.")

# Membuat ID Transaksi secara otomatis
def buat_id_transaksi(nama_cs, counter):
    tanggal = datetime.date.today().strftime("%y%m%d")
    return f"{nama_cs}{tanggal}-{counter:03d}"

# Menyimpan struk belanja ke dalam file CSV
def simpan_struk_ke_csv(nama_file, belanjaan, total_belanja, uang_tunai, kembali):
    with open(nama_file, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["KEJORA SHOP"])
        writer.writerow([nama_file.split('.')[0]])
        writer.writerow([])
        writer.writerow(["ITEM", "JUMLAH", "HARGA", "TOTAL HARGA"])
        writer.writerow([])

        for belanja in belanjaan:
            jumlah = belanja["jumlah"]
            item = belanja["item"]
            harga = belanja["harga"]
            total_harga = hitung_total_harga(jumlah, harga)
            writer.writerow([item.upper(), jumlah, format_harga(harga), format_harga(total_harga)])

        writer.writerow([])
        writer.writerow(["TOTAL BELANJA", "", "", format_harga(total_belanja)])
        writer.writerow(["UANG TUNAI", "", "", format_harga(uang_tunai)])
        writer.writerow(["KEMBALIAN", "", "", format_harga(kembali)])
        writer.writerow([])
        writer.writerow(["TERIMAKASIH DAN SELAMAT BERBELANJA LAGI"])

def transaksi_belanja():
    belanjaan = []

    total_belanja = 0
    print("Kejora Shop")

    # Input nama panggilan CS
    nama_cs = input_cs_name("Nama panggilan CS: ")

    # Input counter untuk ID transaksi
    counter = input_counter("No. Transaksi: ")

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
        id_transaksi = buat_id_transaksi(nama_cs, counter)

        # Membuat nama file struk
        nama_file = f"{id_transaksi}.csv"

        simpan_struk_ke_csv(nama_file, belanjaan, total_belanja, uang_tunai, kembali)

        print("\nStruk telah disimpan ke dalam file '{nama_file}'.\n")
        print("Terima kasih telah berbelanja di Kejora Shop!")
    else:
        print("Belanjaan kosong. Transaksi dibatalkan.")


if __name__ == '__main__':
    transaksi_belanja()
