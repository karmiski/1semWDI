def czy_istnieje_prostokat(dane):
    for i in range(len(dane) - 3):
        for j in range(i + 1, len(dane) - 2):
            for k in range(j + 1, len(dane) - 1):
                for l in range(k + 1, len(dane)):
                    x1, y1 = dane[i]
                    x2, y2 = dane[j]
                    x3, y3 = dane[k]
                    x4, y4 = dane[l]

                    # Sprawdź czy punkty tworzą prostokąt
                    if (x1 == x2) and (x3 == x4) and (y1 == y3) and (y2 == y4) and (x1 != x3) and (y1 != y2):
                        # Sprawdź czy są równej długości
                        if (y2 - y1) == (y4 - y3) and (x3 - x1) == (x4 - x2) and (y2 - y1) != (x4 - x2):
                            check = 0
                            for xd in range(i+1,l-1):
                                if(xd !=j and xd !=k):
                                    if(x1 < dane[xd][0] < x3) and (y1 < dane[xd][1] < y2):
                                        check = -1
                                        break
                            if(check == 0):
                                return True

    return False

# Przykładowe dane
dane = [(0, 0), (0, 2), (3, 0), (3, 2), (1, 1), (2, 1), (1, 3), (2, 3), (4,5), (4,7), (5,5),(5,7)]

# Wywołanie funkcji
dane.sort()
wynik = czy_istnieje_prostokat(dane)
print(wynik) 