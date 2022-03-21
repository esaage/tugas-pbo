# Implementasi Overloading

class Mahasiswa:
    def __init__(self, nama, nim):
            self.nama = nama
            self.nim = nim
    
    def tampilMhs(self):
        print("Nama : ", self.nama, ", nim :", self.nim)

    # method overloading
    def hitungSks(self, jmlsks = None, sks = None):
        if jmlsks != None and sks != None:
            totalsks = jmlsks + sks
            print("Total SKS = ", totalsks)
        else : 
            totalsks = jmlsks
            print("Total SKS = ", totalsks)

# memanggil class
mhs1 = Mahasiswa("Erren", 2000)
mhs2 = Mahasiswa("Luffy", 6000)

mhs1.tampilMhs()
mhs2.tampilMhs()

mhs1.hitungSks(80, 34)  # overloading
mhs2.hitungSks(83)        # overloading