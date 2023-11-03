'''Proszę napisać program, 
który metodą sita Eratostenesa wyznaczy liczby pierwsze mniejsze od N(wczytywane). 
Należy obsłużyć wyjątek wczytania liczby, która nie jest naturalna 
i podać ilorazy całkowite i reszty kolejnych wyznaczonych liczb pierwszych, 
przy założeniu, że dzielimy większą liczbę przez mniejszą. '''
try:
    a = int(input())
    if a < 4:
        print('Zbyt mała liczba żeby coś wypisywać')
    else:
        sieve = [0 for i in range(a)] #from 0 to a - 1
        prime = []
        sieve[1] = 1 
        #znajdowanie liczb pierwszych mniejszych od a
        for i in range(2,a):
            x = i
            if sieve[x] == 0:#jeśli liczba nie jest pierwsza to jej wielokrotności zostały wcześniej obsłużone
                prime.append(x)
                while x < a:  #jeśli liczba jest pierwsza to jej wielokrotności nie są
                    sieve[x] = 1
                    x += i
        #wypisanie oczekiwanego wyniku
        for i in range(len(prime)-1,0, -1):
            temp = prime[i]%prime[i-1]
            print(prime[i],'/',prime[i-1],'=',int((prime[i]-temp)/prime[i-1]),' r =', temp)
except:
    print('Wprowadź liczbę naturalną')