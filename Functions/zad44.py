# Definiuje funkcję rekurencyjną 'factorial', która przyjmuje liczbę całkowitą nieujemną 'n'
def factorial(n):
    # Warunek bazowy (stopu): zgodnie z definicją matematyczną silnia z 0 oraz silnia z 1 wynoszą 1.
    # Ten warunek zatrzymuje dalsze wywoływanie funkcji przez samą siebie.
    if n == 0 or n == 1:
        return 1
        
    # Krok rekurencyjny: dla liczb większych od 1 funkcja mnoży bieżącą liczbę 'n'
    # przez wynik silni dla liczby o jeden mniejszej (n - 1)
    if n > 1:
        return n * factorial(n - 1)

# Wywołuje funkcję dla liczby 5 i wypisuje wynik na ekranie ("5! = 120")
print("5! =", factorial(5))