# Definiuje funkcję 'f', która przyjmuje liczbę całkowitą 'n' (określającą końcową liczbę ciągu)
def f(n):
    # range(1, n + 1) -> generuje kolejne liczby całkowite od 1 do 'n' włącznie
    # str(i)            -> zamienia każdą wygenerowaną liczbę 'i' na tekst (napis)
    # "".join(...)      -> łączy wszystkie te napisy w jeden ciąg, używając pustego separatora "" (bez spacji)
    return "".join(str(i) for i in range(1, n + 1))