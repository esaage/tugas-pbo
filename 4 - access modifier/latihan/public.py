class segitiga:
    def __init__(self, alas, tinggi) -> None:
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi


hitung = segitiga(100, 80)

print('Alas segitita = ', hitung.alas)
print('Tinggi segitiga = ', hitung.tinggi)
print('Luas segitiga = ', hitung.luas)