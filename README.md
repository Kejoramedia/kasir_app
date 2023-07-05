# Aplikasi Kasir Kasir_App

Kasir_App adalah aplikasi sederhana yang digunakan untuk melakukan transaksi belanja. Aplikasi ini ditulis dengan Python 3.11 dan menggunakan format CSV untuk menyimpan struk belanja. Anda bisa mengganti "KEJORA SHOP" dengan cara mengedit isi file main.py (ganti KEJORA SHOP dengan nama toko atau bisnis Anda).

## Fungsi Utama

### `transaksi_belanja()`

Fungsi ini menginisiasi proses transaksi belanja. Pengguna (CS/Customer Service) akan diminta untuk memasukkan beberapa informasi, seperti nama panggilan CS dan nomor transaksi. Selanjutnya, pengguna dapat memasukkan item belanjaan beserta harga dan jumlahnya. Setelah semua item dimasukkan, aplikasi akan menampilkan struk belanja dan menghitung total belanja. Pengguna juga diminta untuk memasukkan jumlah uang tunai yang diberikan customer. Aplikasi akan menghitung kembalian dan menyimpan struk belanja ke dalam file CSV. Nama file CSV akan tersimpan dalam format seperti berikut: 

DONI230705-019.csv. (DONI:nama panggilan CS, 230705-019:ID Transaksi, 230705 adalah tanggal transaksi yang akan tercetak otomatis dan 019 adalah nomor transaksi yang harus diinput CS)

Berikut contoh output pada struk file .csv:

KEJORA SHOP
DONI230705-019

ITEM,JUMLAH,HARGA,TOTAL HARGA

AYAM GORENG,5,"Rp.23,500","Rp.117,500"
SATE KAMBING,20,"Rp.7,500","Rp.150,000"
ES JERUK,5,"Rp.10,000","Rp.50,000"

TOTAL BELANJA,,,"Rp.317,500"
UANG TUNAI,,,"Rp.350,000"
KEMBALIAN,,,"Rp.32,500"

TERIMAKASIH DAN SELAMAT BERBELANJA LAGI



## Fungsi Tambahan

### `hitung_total_harga(jumlah, harga)`

Fungsi ini digunakan untuk menghitung total harga suatu item berdasarkan jumlah dan harga per item.

### `format_harga(harga)`

Fungsi ini mengubah harga menjadi format string yang sesuai dengan mata uang rupiah. Format harga yang dihasilkan adalah "Rp.xxxxxx".

### `input_angka(prompt)`

Fungsi ini menerima input angka bulat dari pengguna. Jika pengguna memasukkan input yang bukan angka, pesan kesalahan akan ditampilkan.

### `input_item(prompt)`

Fungsi ini menerima input nama item dari pengguna dan mengubahnya menjadi huruf kapital.

### `input_cs_name(prompt)`

Fungsi ini menerima input nama panggilan CS dari pengguna. Input harus berupa huruf saja, jika tidak, pesan kesalahan akan ditampilkan.

### `input_counter(prompt)`

Fungsi ini menerima input counter untuk ID transaksi. Input harus berupa angka 3 digit, jika tidak, pesan kesalahan akan ditampilkan.

### `buat_id_transaksi(nama_cs, counter)`

Fungsi ini menghasilkan ID transaksi secara otomatis berdasarkan nama panggilan CS dan counter. ID transaksi terdiri dari nama panggilan CS, tanggal hari ini dalam format "yymmdd", dan counter dengan panjang 3 digit.

### `simpan_struk_ke_csv(nama_file, belanjaan, total_belanja, uang_tunai, kembali)`

Fungsi ini digunakan untuk menyimpan struk belanja ke dalam file CSV. Struk berisi informasi tentang item belanjaan, jumlah, harga, total harga, total belanja, uang tunai yang diberikan, kembalian, dan pesan terima kasih.

## Instalasi dan Persyaratan
Sebelum menggunakan aplikasi ini, pastikan Anda telah memenuhi persyaratan berikut:

Python: Pastikan Python 3.11 sudah terinstal di komputer Anda. Jika belum, Anda dapat mengunduh dan menginstal Python dari situs resmi Python (https://www.python.org).

Library csv: Library ini termasuk dalam instalasi standar Python, sehingga tidak perlu menginstalnya secara terpisah.

## Cara Menggunakan Aplikasi

Berikut adalah langkah-langkah untuk menggunakan Kasir_App ini:

1. Unduh file script aplikasi Kasir. Simpan file di direktori yang diinginkan.

2. Buka terminal atau command prompt di komputer Anda.

3. Jalankan terminal atau command prompt, lalu arahkan ke direktori tempat Anda menyimpan file script aplikasi Kasir.

4. Jalankan aplikasi dengan mengikuti petunjuk di bawah ini.


### Langkah-langkah Penggunaan:

1. Nama Panggilan Customer Service (CS)
   - Pertama-tama, Anda akan diminta untuk memasukkan nama panggilan CS. Pastikan untuk memasukkan nama menggunakan huruf saja.
   - Masukkan nama panggilan CS dan tekan Enter.

2. Nomor Transaksi
   - Selanjutnya, Anda diminta untuk memasukkan nomor transaksi dalam bentuk angka tiga digit.
   - Masukkan nomor transaksi dan tekan Enter.

3. Input Item
   - Aplikasi akan meminta Anda untuk memasukkan item yang akan dibeli.
   - Ketikkan nama item yang ingin dibeli dan tekan Enter. Jika Anda ingin mengakhiri transaksi, ketikkan "0" dan tekan Enter.

4. Harga Item
   - Setelah memasukkan item, Anda diminta untuk memasukkan harga item dalam format Rupiah.
   - Ketikkan harga item dan tekan Enter.

5. Jumlah Item
   - Setelah memasukkan harga item, Anda diminta untuk memasukkan jumlah item yang akan dibeli.
   - Ketikkan jumlah item dan tekan Enter.

6. Melanjutkan Transaksi
   - Anda dapat mengulangi langkah 3 hingga 5 untuk menambah item lainnya. Jika tidak ada lagi item yang ingin ditambahkan, ketikkan "0" dan tekan Enter.

7. Struk Belanja
   - Setelah Anda selesai memasukkan semua item yang ingin dibeli, aplikasi akan menampilkan struk belanjaan Anda.
   - Struk belanjaan akan mencantumkan item, harga per item, jumlah item, dan total harga untuk setiap item.
   - Jumlah total belanja juga akan ditampilkan.

8. Uang Tunai
   - Selanjutnya, Anda diminta untuk memasukkan jumlah uang tunai yang diberikan oleh pelanggan.
   - Ketikkan jumlah uang tunai dan tekan Enter.

9. Kembali
   - Aplikasi akan menghitung jumlah kembalian yang harus diberikan kepada pelanggan.
   - Jumlah kembalian akan ditampilkan.

10. Simpan Struk
    - Aplikasi akan secara otomatis membuat ID transaksi dan nama file untuk struk belanjaan Anda.
    - Struk belanjaan beserta total belanja, uang tunai, dan kembalian akan disimpan dalam file CSV.
    - Nama file akan mencantumkan ID transaksi.
    - Struk belanjaan akan disimpan dalam format yang sesuai dengan mata uang Rupiah.

11. Selesai
    - Transaksi telah selesai, dan struk belanjaan telah disimpan dalam file CSV.
    - Aplikasi akan menampilkan pesan konfirmasi bahwa struk telah disimpan dalam file CSV dengan nama yang sesuai.

### Catatan Penting

1. Pastikan Anda telah menginstal Python versi 3.11 untuk menjalankan aplikasi ini.
2. Pastikan ketika menjalankan aplikasi ini melalui CLI, Anda menjalankannya di direktori di mana file aplikasi disimpan.
2. Perhatikan format yang benar saat memasukkan harga item dan jumlah item (harus berupa angka bulat).
3. Pastikan nama panggilan CS terdiri dari huruf saja, tanpa angka atau karakter khusus.
4. Aplikasi akan otomatis membuat ID transaksi dan nama file struk berdasarkan input yang diberikan. Pastikan tidak ada kesalahan dalam input untuk mencegah terjadinya duplikasi ID transaksi.
5. Struk belanja akan disimpan dalam file CSV dengan format yang sesuai dengan mata uang Rupiah.
