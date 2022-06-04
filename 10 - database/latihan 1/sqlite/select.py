from connect import db, cursor

# gaji
cursor.execute("SELECT * FROM `gaji`")

# golongan
cursor.execute("SELECT * FROM `golongan`")

# jabatan
cursor.execute("SELECT * FROM `jabatan`")

# pegawai
cursor.execute("SELECT * FROM `pegawai`")
db.commit()