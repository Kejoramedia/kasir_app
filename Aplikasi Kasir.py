import pandas as pd

def hitung_total_harga(jumlah, harga):
    return jumlah * harga

def format_harga(harga):
    return f"Rp.{harga:,.0f}"

def cetak_struk(jumlah, item, harga):
    total_harga = hitung_total_harga(jumlah, harga)
    return f"{jumlah} {item}\t\t{format_harga(harga)}\t\t{format_harga(total_harga)}"

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
        struk_data = []

        for belanja in belanjaan:
            jumlah = belanja['jumlah']
            item = belanja['item']
            harga = belanja['harga']

            total_harga = hitung_total_harga(jumlah, harga)
            total_belanja += total_harga

            struk = cetak_struk(jumlah, item, harga)
            struk_data.append([jumlah, item, format_harga(harga), format_harga(total_harga)])

        struk_data.append(["", "Total Belanja", "", format_harga(total_belanja)])

        df = pd.DataFrame(struk_data, columns=["Jumlah", "Item", "Harga", "Total Harga"])
        writer = pd.ExcelWriter("struk.xlsx", engine="openpyxl")
        df.to_excel(writer, index=False, sheet_name="Struk")
        writer.book.save("struk.xlsx")  # Menggunakan metode .save() pada writer.book
        writer.close()  # Menutup objek writer

        while True:
            try:
                uang_tunai = int(input("\nUang Tunai: Rp."))
                break
            except ValueError:
                print("Uang tunai harus dalam bentuk angka. Silakan coba lagi.")

        kembali = uang_tunai - total_belanja

        print(f"\n\t\tUang Tunai\t{format_harga(uang_tunai)}")
        print(f"\n\t\tKembali\t\t{format_harga(kembali)}")
    else:
        print("Belanjaan kosong. Transaksi dibatalkan.")
