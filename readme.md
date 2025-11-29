============================================================
APLIKASI PAYROLL KARYAWAN DENGAN ENKRIPSI XOR STREAM CIPHER
============================================================

Aplikasi ini adalah simulasi sistem penggajian (Payroll) sederhana
yang menerapkan keamanan data menggunakan teknik kriptografi.
Gaji karyawan disimpan dalam database MySQL dalam keadaan
terenkripsi (Ciphertext) sehingga tidak bisa dibaca tanpa kunci.

Tugas Sesi 6 : Implementasi Kriptografi

------------------------------------------------------------
A. STRUKTUR FILE
------------------------------------------------------------
1. main.py       : Program utama yang berisi menu antarmuka.
2. koneksi.py    : Mengatur koneksi ke database MySQL.
3. utils.py      : Berisi rumus XOR dan fungsi baca file kunci.
4. setup_db.py   : Script otomatis untuk membuat database & tabel.
5. key.txt       : File rahasia berisi password sistem.

------------------------------------------------------------
B. PERSYARATAN SISTEM (REQUIREMENTS)
------------------------------------------------------------
1. Python 3.x terinstall di komputer.
2. MySQL Server (XAMPP / Laragon / MySQL Workbench).
3. Library Python: mysql-connector-python.

------------------------------------------------------------
C. CARA INSTALL & MENJALANKAN
------------------------------------------------------------

LANGKAH 1: Install Library
Buka Terminal / CMD / PowerShell dan ketik:
   pip install mysql-connector-python

LANGKAH 2: Konfigurasi Database
Buka file "koneksi.py" dan "setup_db.py", pastikan password
MySQL sesuai dengan komputer.
Contoh: password="paramadaksa" (atau kosong "" jika default XAMPP).

LANGKAH 3: Buat File Kunci
Buat file baru bernama "key.txt" di dalam folder proyek ini.
Isi dengan satu kata sandi rahasia.
Contoh isi file key.txt:
   admin123

LANGKAH 4: Jalankan Program
Ketik perintah berikut di terminal:
   python main.py

*Catatan: Saat pertama kali dijalankan, program akan otomatis
 membuat database 'db_payroll' dan tabel 'karyawan'.

------------------------------------------------------------
D. PANDUAN PENGGUNAAN
------------------------------------------------------------
1. Input Karyawan (Create)
   - Masukkan Nama, Jabatan, dan Gaji.
   - Gaji otomatis dienkripsi menggunakan password dari key.txt.

2. Lihat Data Terenkripsi (Public View)
   - Menampilkan data gaji apa adanya dari database.
   - Gaji akan terlihat sebagai kode acak (Hexadecimal).
   - Membuktikan bahwa data aman dari orang asing.

3. Lihat Data Asli (Admin View)
   - Anda diminta memasukkan Password secara manual.
   - Password harus SAMA PERSIS dengan isi file key.txt.
   - Jika benar, gaji akan didekripsi menjadi angka Rupiah.

4. Hapus Data (Delete)
   - Memerlukan verifikasi password sebelum menghapus.

------------------------------------------------------------
E. TEKNIS KEAMANAN
------------------------------------------------------------
- Algoritma: XOR Stream Cipher.
- Penyimpanan: Ciphertext dikonversi ke Hexadecimal string
  agar aman disimpan di tipe data VARCHAR database.
- Key Management: Kunci dipisah dalam file fisik (key.txt)
  untuk mensimulasikan keamanan server.

============================================================
Dibuat dengan Python & MySQL Connector
Oleh : Zelda Elisa Hijry - 230401010046
============================================================