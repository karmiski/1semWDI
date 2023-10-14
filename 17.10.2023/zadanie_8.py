import random
h = input()
h = int(h)
s = 1
while h > 0:
    for i in range(h):
        print(' ', end='')
    x = random.randrange(0,s)
    for i in range(s):
        if(s == 1):
            print('X', end='')
        elif i == x:
            print('0', end='')    
        else:
            print('*', end='')
    print('')
    h-=1
    s+=2    
#pien
for i in range(int((s-3)/2 + 1)):
    print(' ', end='')
print('U')
