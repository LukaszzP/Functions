# Definiuje funkcję 'f', która przyjmuje numer wyrazu ciągu 'n'
def f(n):
    # Jeśli szukamy 1. wyrazu ciągu, funkcja od razu zwraca 0
    if n == 1:
        return 0
    # Jeśli szukamy 2. wyrazu ciągu, funkcja od razu zwraca 1
    if n == 2:
        return 1
    
    # Tworzy dwie zmienne przechowujące dwa ostatnie wyrazy ciągu (startuje od 1. i 2. wyrazu)
    a, b = 0, 1
    
    # Pętla wykonująca się od 3. wyrazu aż do n-tego wyrazu włącznie
    for _ in range(3, n + 1):
        # Jednocześnie aktualizuje obie zmienne:
        # nowa wartość 'a' staje się dotychczasowym 'b',
        # a nowa wartość 'b' staje się sumą poprzednich dwóch wyrazów (a + b)
        a, b = b, a + b
        
    # Po zakończeniu pętli zwraca wartość n-tego wyrazu zapisaną w zmiennej 'b'
    return b