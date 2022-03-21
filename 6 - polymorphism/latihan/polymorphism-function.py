# Polymorphism dengan function

print(len("Polymorphism"))
print(len([0,1,2,3]))

# menggunakan class
class Jerman:
    def ibukota(self):
        print("Berlin adalah ibu kota jerman")

class Jepang:
    def ibukota(self):
        print("Tokyo adalah ibu kota jepang")

negara1 = Jerman()
negara2 = Jepang()

for country in (negara1, negara2):
    print(country.ibukota())