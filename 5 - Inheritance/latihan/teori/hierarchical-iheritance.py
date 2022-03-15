# Esa Age 
# 5210411159

# parent
class induk:
    def fungsiInduk(self):
        print('Fungsi Induk')

# child class 1
class anak1(induk):
    def fungsiAnak1(self):
        print('Fungsi Anak Pertama')


# child class 2
class anak2(induk):
    def fungsiAnak2(self):
        print('Fungsi Anak Kedua')

a1 = anak1()
a2 = anak2()

a1.fungsiAnak1()
a1.fungsiInduk()

a2.fungsiAnak2()
a2.fungsiInduk()