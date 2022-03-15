# Esa Age 
# 5210411159

# Class Parent 
class hewan:
    def bersuara(self):
        print("Kucin Bersuara ")


# child class dari hewan
class kucing(hewan):
    def suara(self):
        print('Meong')

# child class dari kucing
class anakKucing(kucing):
    def minum(self):
        print('Susu')


k=anakKucing()
k.bersuara()
k.suara()
k.minum()