#Mengupdate asal dari hewan 'Komodo' menjadi 'Nusa
import sqlite3
koneksi = sqlite3.connect('database_hewan.db')
kursor = koneksi.cursor()

id_hewan = 3

kursor.execute(f'UPDATE HEWAN SET asal = "Nusa Tenggara Timur" WHERE id_hewan = {id_hewan}')
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data pegawai dengan ID {id_hewan} berhasil diupdate.")
else:
    print(f"Tidak ada data pegawai dengan ID {id_hewan}.")

koneksi.close()
