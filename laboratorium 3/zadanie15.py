'''
Zadanie 15.
Utwórz macierz o wymiarach (2n−1)×(2n−1)wypełnioną zerami. Napisz funkcje umożliwiające:
    tworzenie obramowania (brzegi marcierzy) wprowadzoną przez użytkownika liczbą,
    uzupełnienie przekątnych wprowadzoną przez użytkownika liczbą (osobno dla każdej przekątnej i razem),
    tworzenie obramowania wprowadzoną przez użytkownika liczbą na zmianę z 0.
'''
try:
    a = int(input("Wprowadź liczbę naturalną:"))
    if(a < 2):
        int('a')
    b = int(input("Czym chcesz wypełniać?"))
except:
    print("Obie liczby powinny być całkowite, a > 1")
    exit()

matrix = [[0 for i in range(2*a-1)] for j in range(2*a-1)]

def printm(matrix):
    for i in range(2*a-1):
        for j in range(2*a-1):
            print(matrix[i][j],end="")
            matrix[i][j] = 0
        print("")

def ramka(parity1,parity2):
    for i in range(2*a-1):
        temp = max((parity1+i)%2 * b, (parity2+i)%2 * b) #gdy chociaż jedna jest jedynką to nie ma możliwości zera
        matrix[i][0], matrix[i][2*a-2], matrix[0][i], matrix[2*a-2][i] = temp,temp,temp,temp
    printm(matrix)

def przek(l,r): #lewa i prawa przekątna osobno
    for i in range(2*a-1):
        if(l == 1):
            matrix[i][i] = b
        if(r == 1):
            matrix[i][(2*a-2)-i] = b
    printm(matrix)

option = -1
while(0 == 0):
    print("Wybierz opcję:\n0: wyjście\n1:tworzenie obramowania \n2:tworzenie obramowania na zmianę z 0\n3:uzupełnienie przekątnych\n4:przekątna od 0,0\n5:przekątna od n-2,0")
    try:
        option = int(input())
        if(option > 5 or option < 0):
            int('a')
    except:
        print("Wybierz opcję z zakresu od -1 do 6")
      
    if(option == 2):  #obramowanie naprzemienne
        ramka(1,1)
    elif(option == 1):
        ramka(0,1)
    elif(option == 3): #przekątne 3x
        przek(1,1)
    elif(option == 4): 
        przek(1,0)
    elif(option == 5):    
        przek(0,1)
    elif(option == 0): #wyjście
        exit()
    else: #jak to lepiej zrobić?
        a = a