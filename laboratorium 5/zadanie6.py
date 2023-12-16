class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def czy_istnieje_prostokat(dane):
    for i in range(len(dane) - 3):
        for j in range(i + 1, len(dane) - 2):
            for k in range(j + 1, len(dane) - 1):
                for l in range(k + 1, len(dane)):
                    p1 = dane[i]
                    p2 = dane[j]
                    p3 = dane[k]
                    p4 = dane[l]

                    # Sprawdź czy punkty tworzą prostokąt
                    if (p1.x == p2.x) and (p3.x == p4.x) and (p1.y == p3.y) and (p2.y == p4.y) and (p1.x != p3.x) and (p1.y != p2.y):
                        # Sprawdź czy są równej długości
                        if (p2.y - p1.y) == (p4.y - p3.y) and (p3.x - p1.x) == (p4.x - p2.x) and (p2.y - p1.y) != (p4.x - p2.x):
                            check = 0
                            for xd in range(i+1, l-1):
                                if xd != j and xd != k:
                                    if (p1.x < dane[xd].x < p3.x) and (p1.y < dane[xd].y < p2.y):
                                        check = -1
                                        break
                            if check == 0:
                                return True

    return False

# Przykładowe dane
dane = [Point(0, 0), Point(0, 2), Point(3, 0), Point(3, 2), Point(1, 1), Point(2, 1), Point(1, 3), Point(2, 3),
        Point(4, 5), Point(4, 7), Point(5, 5), Point(5, 7)]

# Wywołanie funkcji
dane.sort(key=lambda p: (p.x, p.y))
wynik = czy_istnieje_prostokat(dane)
print(wynik)