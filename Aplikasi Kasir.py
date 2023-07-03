def hitung_total_harga(jumlah, harga):
    return jumlah * harga


def cetak_struk(jumlah, item, harga):
    total_harga = hitung_total_harga(jumlah, harga)
    return f"{jumlah} {item}\t\tRp.{harga}\t\tRp. {total_harga}"


if __name__ == '__main__':
    belanjaan = []

    while True:
        jumlah = int(input("Jumlah (Ketik 0 transaksi selesai): "))
        item = str(input("Item: "))
        harga = int(input("Harga: Rp."))

        belanjaan.append({"jumlah": jumlah, "item": item, "harga": harga})

        lanjut = input("Apakah ada item belanjaan lain? (y/n): ")
        if lanjut.lower() != 'y':
            break

    total_belanja = 0

    for belanja in belanjaan:
        jumlah = belanja['jumlah']
        item = belanja['item']
        harga = belanja['harga']

        total_harga = hitung_total_harga(jumlah, harga)
        total_belanja += total_harga

        print(cetak_struk(jumlah, item, harga))

    print("-----------------------------------------------")
    print(f"\t\tTotal Belanja\tRp.{total_belanja}")

    uang_tunai = int(input("\nUang Tunai: Rp."))
    kembali = uang_tunai - total_belanja

    print(f"\n\t\tUang Tunai\tRp.{uang_tunai}")
    print(f"\n\t\tKembali\t\tRp.{kembali}")
