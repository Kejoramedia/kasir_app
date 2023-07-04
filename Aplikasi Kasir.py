import csv

def hitung_total_harga(jumlah, harga):
    return jumlah * harga

def format_harga(harga):
    return f"Rp.{harga:,.0f}"

if __name__ == '__main__':
    belanjaan = []

    while True:
        item = input('Item (Ketik "0" untuk menyelesaikan transaksi): ').title()

        if item == "0":
            break

        while True:
            try:
                harga = int(input("Harga: Rp."))
                break
            except ValueError:
                print("Harga harus angka bulat. Silakan coba lagi.")

        while True:
            try:
                jumlah = int(input("Jumlah: "))
                break
            except ValueError:
                print("Jumlah harus angka bulat. Silakan coba lagi.")

        belanjaan.append({"jumlah": jumlah, "item": item, "harga": harga})

    if belanjaan:
        total_belanja = 0

        print("\nStruk Belanja:")
        print("-----------------------------------------------")
        for belanja in belanjaan:
            jumlah = belanja['jumlah']
            item = belanja['item']
            harga = belanja['harga']

            total_harga = hitung_total_harga(jumlah, harga)
            total_belanja += total_harga

            print(f"{jumlah} {item}\t\t{format_harga(harga)}\t\t{format_harga(total_harga)}")

        print("-----------------------------------------------")
        print(f"Total Belanja:\t{format_harga(total_belanja)}")

        while True:
            try:
                uang_tunai = int(input("\nUang Tunai: Rp."))
                break
            except ValueError:
                print("Uang tunai harus dalam bentuk angka. Silakan coba lagi.")

        kembali = uang_tunai - total_belanja

        print(f"Kembali: {format_harga(kembali)}")

        # Menyimpan struk ke file CSV
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
            writer.writerow({"Item": "Total Belanja", "Jumlah": "", "Harga": "", "Total Harga": format_harga(total_belanja)})
            writer.writerow({"Item": "Uang Tunai", "Jumlah": "", "Harga": "", "Total Harga": format_harga(uang_tunai)})
            writer.writerow({"Item": "Kembalian", "Jumlah": "", "Harga": "", "Total Harga": format_harga(kembali)})

    else:
        print("Belanjaan kosong. Transaksi dibatalkan.")
