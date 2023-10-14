l1,l2 = input().split()
l1 = int(l1)
l2 = int(l2)
if l2 == 0:
    print('Nie da się dzielic przez zero')
elif l1 < 0 and l2 < 0:
    print('Obie liczby są ujemne')
else: #na pewno teraz najwyżej jedna liczba jest ujemna więc możemy sprawdzić obie
    if l1 < 0:
        l1 *= -1
    if l2 < 0:
        l2 *= -1
    #wypisujemy 
    print('suma:', l1 + l2)
    print('różnica:', l1 - l2)
    print('iloczyn:', l1 * l2)
    print('iloraz:', l1 * l2)
    print('kwadraty', l1*l1, l2*l2)
    print('pierwiastki:', l1**0.5, l2**0.5 )
    if(l1*l2 == 10):
        print('Yay!')
"""
komentarz w postaci bloku tekstu nie jest tu potrzebny
to jest tak tylko tutaj w ramach podpunktu zadania
"""