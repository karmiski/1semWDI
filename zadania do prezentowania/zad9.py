#Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona. 
N =  10
num = list(range(0,N))
odej = list(range(0,N))
#sito z odwołaniami
for i in range(2,N):
    if(num[i] == i): #prime number
        x = 2*i
        while(x < N):
            #krotności będą liczone wiele razy, więc odejmujemy
            num[x] = int(x/i)  
            x+=i
#sumujemy dzielniki od początku
for i in range(2,N):
    if(num[i] == i): #prime number
        num[i] += 1
    else:
        num[i] = num[num[i]] + i

#sprawdzamy czy są liczby zaprzyjaźnione