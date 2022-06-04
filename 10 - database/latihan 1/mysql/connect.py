from colorama import Fore
import mysql



db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "kuliah-pbop-crud-mysql"
)
cursor = db.cursor()
print(Fore.RED + 'some red text')

print("database terhubung sudah :D")