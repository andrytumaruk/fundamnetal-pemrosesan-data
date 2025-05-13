# ETL Pipeline Project

## 📌 Deskripsi Proyek
Proyek ini merupakan implementasi pipeline ETL (Extract, Transform, Load) untuk mengambil data produk dari situs web Fashion Studio Dicoding, membersihkannya, lalu menyimpan data tersebut ke beberapa repositori penyimpanan: file CSV, Google Sheets, dan database PostgreSQL. Proyek juga dilengkapi dengan unit testing untuk menjamin keandalan pada setiap tahap proses ETL.

## 🚀 Fitur Utama
- Extract: Scraping data produk dari website Fashion Studio Dicoding.

- Transform: Pembersihan dan pemrosesan data, termasuk:

- Konversi harga ke format Rupiah.

- Validasi dan penghapusan entri tidak valid.

- Penyesuaian tipe data.

- Load: Menyimpan data hasil transformasi ke:

- File CSV (products.csv)

- Google Sheets (via Google Sheets API)

-PostgreSQL (menggunakan psycopg2)

-Testing: Unit test untuk masing-masing modul ETL guna memastikan stabilitas dan akurasi proses.

## 🗂️ Struktur & Penjelasan Berkas
### File / Folder	Deskripsi
- main.py	Menjalankan keseluruhan proses ETL dari extract hingga load.
- utils/extract.py	Fungsi untuk melakukan scraping data dari situs web.
- utils/transform.py	Fungsi untuk membersihkan dan memodifikasi data.
- utils/load.py	Fungsi untuk menyimpan data ke CSV, Google Sheets, dan PostgreSQL.
- tests/test_extract.py	Unit test untuk tahap Extract.
- tests/test_transform.py	Unit test untuk tahap Transform.
- tests/test_load.py	Unit test untuk tahap Load.
- products.csv	Output file CSV berisi data produk yang sudah diproses.
- requirements.txt	Daftar dependensi Python yang diperlukan.
- google-sheets-api.json	File kredensial untuk Google Sheets API (tidak diunggah untuk keamanan).

## Dependensi

Sebelum menjalankan proyek, pastikan untuk menginstal dependensi yang diperlukan. Anda dapat menginstalnya dengan menjalankan perintah berikut:

```bash
pip install -r requirements.txt
````

## Cara Menjalankan

1. Pastikan Anda sudah mengaktifkan virtual environment.
2. Jalankan `main.py` untuk mengeksekusi pipeline ETL:

```bash
python main.py
```
atau
```
py main.py
```
3. Data yang telah diproses akan disimpan dalam file `products.csv` dan juga akan dimuat ke dalam Google Sheets.

## Unit Testing

Unit testing dilakukan untuk memastikan setiap fungsi dalam pipeline ETL berjalan sesuai dengan yang diharapkan. 

### Hasil Test Coverage

Berikut adalah hasil test coverage dari proyek ini:

```
Name                      Stmts   Miss  Cover
---------------------------------------------
tests\test_extract.py        21      1    95%
tests\test_load.py           21      1    95%
tests\test_transform.py      20      1    95%
utils\extract.py             25      3    88%
utils\load.py                30     12    60%
utils\transform.py           18      1    94%
---------------------------------------------
TOTAL                       135     19    86%
```

Dengan total coverage **86%**, proyek ini memenuhi kriteria untuk **Advanced** dalam penilaian unit testing.

## Kriteria Penilaian

### Kriteria 1: Membuat ETL Pipeline dengan Prinsip Modular Code

* Kode dibagi menjadi tiga modul terpisah: **Extract**, **Transform**, dan **Load**.
* Mengambil data dari website [https://fashion-studio.dicoding.dev/](https://fashion-studio.dicoding.dev/).
* Data yang diproses mencakup Title, Price, Rating, Colors, Size, dan Gender.
* Data yang diproses telah dibersihkan dan dikonversi sesuai ketentuan, termasuk konversi harga ke dalam mata uang Rupiah (Rp16.000).
* Data yang dihasilkan tidak mengandung nilai null, duplikat, atau invalid.

### Kriteria 2: Menyimpan Data dalam Repositori Data

* Data disimpan dalam format CSV dan juga dimuat ke dalam Google Sheets, dan PostgreSQL.
* Menggunakan Google Sheets API dengan service account yang disediakan.

### Kriteria 3: Menerapkan Unit Test

* Unit testing diterapkan pada setiap tahapan ETL (extract, transform, load).
* Test coverage mencapai **86%**, memenuhi kriteria untuk **Advanced**.
