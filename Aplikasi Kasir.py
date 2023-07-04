import csv

def hitung_total_harga(jumlah, harga):
    return jumlah * harga

def format_harga(harga):
    return f"Rp.{harga:,.0f}"

def input_angka(prompt):
    while True:
        try:
            angka = int(input(prompt))
            return angka
        except ValueError:
            print("Input harus berupa angka bulat. Silakan coba lagi.")

def input_item(prompt):
    return input(prompt).upper()

def simpan_struk_ke_csv(belanjaan, total_belanja, uang_tunai, kembali):
    with open("struk.csv", mode="w", newline="") as file:
        fieldnames = ["Item", "Jumlah", "Harga", "Total Harga"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for belanja in belanjaan:
            jumlah = belanja["jumlah"]
            item = belanja["item"]
            harga = belanja["harga"]
            total_harga = hitung_total_harga(jumlah, harga)
            writer.writerow({"Item": item, "Jumlah": jumlah, "Harga": format_harga(harga), "Total Harga": format_harga(total_harga)})

        writer.writerow({})
        writer.writerow({"Item": "TOTAL BELANJA", "Jumlah": "", "Harga": "", "Total Harga": format_harga(total_belanja)})
        writer.writerow({"Item": "UANG TUNAI", "Jumlah": "", "Harga": "", "Total Harga": format_harga(uang_tunai)})
        writer.writerow({"Item": "KEMBALIAN", "Jumlah": "", "Harga": "", "Total Harga": format_harga(kembali)})


def transaksi_belanja():
    belanjaan = []
    total_belanja = 0

    print("Kejora Shop")
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
            print(f"{item.upper().ljust(15)}{format_harga(harga).ljust(10)}{str(jumlah).ljust(5)}{format_harga(total_harga)}")
        print("---------------------------")
        print(f"Total Belanja:\t{format_harga(total_belanja)}")

        uang_tunai = input_angka("\nUang Tunai: Rp.")
        kembali = uang_tunai - total_belanja

        print(f"Kembali: {format_harga(kembali)}")

        simpan_struk_ke_csv(belanjaan, total_belanja, uang_tunai, kembali)

        print("\nStruk telah disimpan ke dalam file 'struk.csv'.\n")
        print("Terima kasih telah berbelanja di Kejora Shop!")
    else:
        print("Belanjaan kosong. Transaksi dibatalkan.")

if __name__ == '__main__':
    transaksi_belanja()

