#Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona. 
N =  1000000
num = list(range(0,N))
'''
#algorytm najprostszy - O(n*sqrt(n)), dla miliona zbyt wolny
for i in range(2,N):
    a = i
    x = 2
    num[i] = 1
    while(x*x<a):
        if(a%x) == 0:
            num[i] += x + int(a/x)
        x+=1
    if(x*x == a): 
        num[i] += x
for i in range(2,N):
    if(num[i] < N):
        if(num[num[i]] < N):
            if(i == num[num[i]] and i < num[i]):
                print(i,num[i])
'''
for i in range(2,N):
    a = i
    x = 2
    num[i] = 1
    while(x*x<a):
        if(a%x) == 0:
            num[i] += x + int(a/x)
        x+=1
    if(x*x == a): 
        num[i] += x
for i in range(2,N):
    if(num[i] < N):
        if(num[num[i]] < N):
            if(i == num[num[i]] and i < num[i]):
                print(i,num[i])