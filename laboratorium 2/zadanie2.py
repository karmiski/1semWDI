'''Proszę napisać program, 
który metodą sita Eratostenesa wyznaczy liczby pierwsze mniejsze od N(wczytywane). 
Należy obsłużyć wyjątek wczytania liczby, która nie jest naturalna 
i podać ilorazy całkowite i reszty kolejnych wyznaczonych liczb pierwszych, 
przy założeniu, że dzielimy większą liczbę przez mniejszą. '''
try:
    a = int(input())
    sieve = [0 for i in range(a)] #from 0 to a - 1
    prime = []
    sieve[1] = 1 
    #finding primes smaller than a
    for i in range(2,a):
        x = i
        if sieve[x] == 0:
            prime.append(x)
            while x < a:  #if number not prime then its multiplications were already found 
                sieve[x] = 1
                x += i

    for i in range(len(prime)-1,0, -1):
        temp = prime[i]%prime[i-1]
        print(prime[i],'/',prime[i-1],'=',int((prime[i]-temp)/prime[i-1]),'r =', temp)
except:
    print('you should input a natural number')