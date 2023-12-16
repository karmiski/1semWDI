import time
def rek(n):
    if(n == 1):
        return 1
    else:
        return n * rek(n-1)
def iter(n):
    w = 1
    for i in range(1,n+1):
        w*=i
    return w
try:
    n=int(input())
except:
    exit
t1 = time.time()
x1 = rek(n)
t2 = time.time()
x2 = iter(n)
t3 = time.time()
print(t2 - t1, " ", t3 - t2)