# Definiuje funkcję rekurencyjną 'power', która przyjmuje podstawę potęgi ('x') oraz wykładnik ('n')
def power(x, n):
    # Warunek bazowy (stopu): każda liczba podniesiona do potęgi 0 wynosi 1 (x^0 = 1).
    # Zatrzymuje dalsze wywoływanie funkcji przez samą siebie.
    if n == 0:
        return 1
        
    # Krok rekurencyjny: mnoży podstawę 'x' przez wynik potęgowania dla wykładnika mniejszego o 1 (x * x^(n-1))
    return x * power(x, n - 1)

# Wywołuje funkcję dla 5 do potęgi 3 i wypisuje wynik na ekranie ("5^3 = 125")
print("5^3 =", power(5, 3))