'''
Należy napisać program, który umożliwia 
zmianę nazw, kopiowanie, przenoszenie i usuwanie plików 
zgodnie z życzeniem użytkownika. 
'''
import os
import hashlib
#key = input("Podaj klucz:")
try:
    file = open('/home/my_hashed_password.txt', "r")
    password = file.readline()[0:-1]
    print(password)
except:
    print("Brak ustawionego hasła")
    exit()
userpass = hashlib.sha256(input("Podaj hasło:").encode()).hexdigest()
if userpass != password:
    print("Niestety nie")
    exit()
else:
    print("Witaj")
    #no to czas na program
    print(os.getcwd())

