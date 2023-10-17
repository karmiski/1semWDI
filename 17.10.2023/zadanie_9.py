s = 0 #saldo
n = 1
print('Ustaw pin:')
p = input()
while(n == 1):
    print('Co chcesz zrobić w kolejnym kroku? (1-wplata, 2-wyplata, 3-sprawdz stan,4-zakoncz )')
    a = input()
    if(a != '1' and a != '2' and a != '3' and a!='4'):
        print('Zły numerek')
    else:
        a = int(a)
        print('Podaj pin')
        temp = input()
        if temp == p:
            if a == 1 or a == 2: #wplata
                print('Podaj kwotę')
                x = int(input())
                if a == 1:
                    s += x
                if a == 2:
                    if s >= x:
                        s -= x
                    else:
                        print('Brak pieniędzy na koncie')
            elif a == 3:
                print(s)
            else:
                n = 0
        else:
            print('Zły pin')

