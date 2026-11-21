# Definiuje funkcję 'f', która przyjmuje napis reprezentujący liczbę binarną
def f(binary_number):
    # Zwraca True tylko wtedy, gdy spełnione są OBA warunki połączone słowem 'and':
    # 1. all(ch in ('0', '1') for ch in binary_number) -> dla każdego znaku ('ch') w napisie sprawdza, 
    #    czy należy on do zbioru ('0', '1'). Funkcja all() zwraca True, jeśli WSZYSTKIE znaki spełniają ten warunek.
    # 2. len(binary_number) > 0 -> sprawdza, czy napis nie jest pusty (ma długość większą niż 0).
    return all(ch in ('0', '1') for ch in binary_number) and len(binary_number) > 0

# Wywołuje funkcję dla napisu "01010101" i wypisuje wynik na ekranie (w tym przypadku: True)
print((f("01010101")))