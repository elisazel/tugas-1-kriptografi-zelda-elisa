import koneksi
import utils
import setup_db

def create():
    print("\n--- [1] INPUT KARYAWAN BARU ---")
    
    stored_key = utils.get_stored_key()
    if not stored_key:
        print("Error: File key.txt tidak ditemukan. Buat file itu dulu!")
        return

    nama = input("Nama Karyawan : ")
    jabatan = input("Jabatan       : ")
    gaji = input("Gaji Pokok    : ")
    
    enc_gaji = utils.encrypt_hex(gaji, stored_key)

    db = koneksi.get_db()
    cursor = db.cursor()
    sql = "INSERT INTO karyawan (nama, jabatan, gaji_encrypted) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nama, jabatan, enc_gaji))
    db.commit()
    db.close()
    print("Sukses! Data disimpan dalam format terenkripsi.")

def read_encrypted_only():
    db = koneksi.get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nama, jabatan, gaji_encrypted FROM karyawan")
    rows = cursor.fetchall()
    db.close()

    print("-" * 60)
    print(f"{'ID':<3} | {'Nama':<15} | {'Jabatan':<10} | {'Gaji (Ciphertext/Raw)'}")
    print("-" * 60)
    
    for r in rows:
        print(f"{r[0]:<3} | {r[1]:<15} | {r[2]:<10} | {r[3]}")
    
    print("-" * 60)
    print("NOTE: Kolom Gaji tidak terbaca karena Anda melihat tanpa Kunci Rahasia.")

def read_decrypted_with_key():
    input_key = input("Masukkan Password System: ")
    stored_key = utils.get_stored_key()

    if input_key != stored_key:
        print("\n[AKSES DITOLAK] Password salah!")
        return

    db = koneksi.get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nama, jabatan, gaji_encrypted FROM karyawan")
    rows = cursor.fetchall()
    db.close()

    print("-" * 60)
    print(f"{'ID':<3} | {'Nama':<15} | {'Jabatan':<10} | {'Gaji (Terbuka)'}")
    print("-" * 60)
    
    for r in rows:
        dec_gaji = utils.decrypt_hex(r[3], stored_key)
        
        if dec_gaji and dec_gaji.isdigit():
            print(f"{r[0]:<3} | {r[1]:<15} | {r[2]:<10} | Rp {int(dec_gaji):,}")
        else:
            print(f"{r[0]:<3} | {r[1]:<15} | {r[2]:<10} | [Data Corrupt]")

    print("-" * 60)

def delete():
    input_key = input("Masukkan Password Admin: ")
    stored_key = utils.get_stored_key()

    if input_key != stored_key:
        print("Password Salah! Penghapusan dibatalkan.")
        return

    target = input("ID Karyawan yang akan dihapus: ")
    db = koneksi.get_db()
    cursor = db.cursor()
    sql = "DELETE FROM karyawan WHERE id = %s"
    cursor.execute(sql, (target,))
    db.commit()
    
    if cursor.rowcount > 0:
        print("Data berhasil dihapus.")
    else:
        print("ID tidak ditemukan.")
    db.close()

def main():
    setup_db.run_setup()
    
    while True:
        print("\n=== SISTEM PENGGAJIAN (XOR CIPHER) ===")
        print("1. Input Karyawan (Auto Encrypt)")
        print("2. Lihat Data Terenkripsi (Tanpa Key)")
        print("3. Lihat Data Asli (Pakai Key)")
        print("4. Hapus Data")
        print("5. Keluar")
        
        p = input("Pilih Menu: ")
        if p == '1': create()
        elif p == '2': read_encrypted_only()
        elif p == '3': read_decrypted_with_key()
        elif p == '4': delete()
        elif p == '5': break

if __name__ == "__main__":
    main()