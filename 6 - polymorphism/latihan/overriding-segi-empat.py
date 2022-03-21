# Implementasi Overriding

class SegiEmpat():
    def __init__(self, panjang, lebar):
            self.panjang = panjang
            self.lebar = lebar
    
    def hitungLuas(self): # method overriding
        print("Luas Segi empat : ", self.panjang * self.lebar , "m2")

class BujurSangkar(SegiEmpat):
    def __init__(self, sisi):
            self.side = sisi
            SegiEmpat.__init__(self, sisi, sisi)
    
    def hitungLuas(self): # method overriding
        print("Luas Bujur sangkar : ", self.side * self.side , "m2")

b = BujurSangkar(4)
s = SegiEmpat(2,4)
b.hitungLuas()
s.hitungLuas()