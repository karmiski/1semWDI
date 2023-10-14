a = int(input())
b = int(input())
if(b-a > 21): # np 3-1 = 2 ale mamy liczby 1,2,3
    s = (b+a)/2
    if(s%1 == 0.5):
        s+=0.5
    s-=3
    for i in range(3): #0,1,2
        print(s+i)
    if(s+3 == (a+b)/2): #srednia to l naturalna, trzeba ominac
        s+=4
    else: 
        s+=3
    for i in range(0,3):
        print(s+i)
else:
    while a <= b:
        print(a)
        a +=1