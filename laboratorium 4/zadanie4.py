'''
Należy napisać program, który umożliwia 
zmianę nazw, kopiowanie, przenoszenie i usuwanie plików 
zgodnie z życzeniem użytkownika. 
'''
import os
import shutil
import hashlib

def select(arg):  #1 - directories, 0 - others
        if(arg == 1):
            print("Gdzie?:")
            lista = [d for d in os.listdir(path) if os.path.isdir(path + "/" + d)]
        else:
            print("Wybierz sobie:")
            lista = [d for d in os.listdir(path) if (os.path.isdir(path + "/" + d) == False)]
        a = 0
        for item in lista:
            print(a,": ",item)
            a+=1
        if(len(lista) == 0):
            print("Tu nic nie ma")  #excepta wyrzuca potem, dodaj try
        else:
            try:
                return(lista[int(input())])
            except:
                exit()
try:
    file = open('/home/my_hashed_password.txt', "r")
    password = file.readline()[0:-1]
    print(password)
except:
    print("Brak ustawionego hasła")
    exit()
'''userpass = hashlib.sha256(input("Podaj hasło:").encode()).hexdigest()
if userpass != password:
    print("Niestety nie")
    exit()
else:'''
if(0==0):
    print("Witaj")
    path = os.getcwd()
    trash = path + "/trash"
    #no to czas na program
    while(0==0):
        print("Jesteś tutaj:\n",path,"\nCo chcesz zrobić?\n1:<\n2:>\n3:usuń\n4:kopiuj\n5:wklej\n6:zmień nazwę\n")
        try:
            a = int(input())
        except:
            exit()
        if(a == 1): #<
            try:
                path = os.path.dirname(path)
            except:
                print("Co ty robisz?")
        elif(a == 2): #>
            item = select(1) 
            path = path + "/" + item
        elif(a == 3): #usuń
            item = select(0)
            shutil.move(path + "/" + item, trash+"/"+item)
        elif(a == 4): #kopiuj
            clipboard = select(0)
            clippath = path + "/" + clipboard
        elif(a == 5): #wklej
            shutil.move(clippath,path+"/"+clipboard)
        elif(a == 6): #zmień nazwę
            item = select(0)
            newname = input("Podaj nową nazwę:")
            os.rename(path + "/" + item, newname)
        else:
            exit()

