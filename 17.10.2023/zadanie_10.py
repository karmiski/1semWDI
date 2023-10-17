import random
n = 1
while(n == 1):
    try:
        a = float(input('Podaj liczbę: '))
        b = float(input('Podaj liczbę: '))
    except:
        print('Następnym razem podaj liczby')
    z = input('Podaj tryb: ')
    if z == '+':
        print(a+b)
    elif z == '-':
        print(a-b)
    elif z == '*':
        print(a*b)
    elif z == '/':
        if b == 0:
            print('Nie dziel przez zero')
        else:
            print(a/b)
    elif z == '#':
        print(a**(1/b))
    elif z == '^':
        print(a**b)
    elif z == 'x':
        if a > b:
            a,b = b,a
        print(random.randrange(a,b))
    n = 2
    while n == 2:
        x = input('Czy chcesz wprowadzić nowe dane?')
        if x == 'N':
            n = 0
        elif x == 'T':
            n = 1
        else:
            print('Podaj T lub N')