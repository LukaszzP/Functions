# Definiuje funkcję 'f', która przyjmuje trzy liczby jako argumenty: n1, n2 oraz n3
def f(n1, n2, n3):
    # Sprawdza trzy warunki połączone operatorem logicznym 'or' (LUB):
    # czy n1 jest mniejsze od 0, LUB n2 jest mniejsze od 0, LUB n3 jest mniejsze od 0.
    # Zwraca True, jeśli choć jeden z tych warunków jest spełniony, w przeciwnym razie False.
    return n1 < 0 or n2 < 0 or n3 < 0