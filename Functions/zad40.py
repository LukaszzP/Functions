# Definiuje funkcję 'f', która przyjmuje początek ('x') i koniec ('y') przedziału liczbowego
def f(x, y):
    # Zmienna przechowująca sumę znalezionych liczb (na początku 0)
    total = 0
    
    # Pętla przechodzi kolejno przez wszystkie liczby całkowite od 'x' do 'y' włącznie
    for num in range(x, y + 1):
        # Sprawdza trzy warunki jednocześnie (operator 'and'):
        # 1. num % 2 == 0 -> liczba dzieli się bez reszty przez 2
        # 2. num % 3 == 0 -> liczba dzieli się bez reszty przez 3
        # 3. num % 4 != 0 -> reszta z dzielenia przez 4 jest różna od zera (nie dzieli się przez 4)
        if num % 2 == 0 and num % 3 == 0 and num % 4 != 0:
            # Jeśli wszystkie trzy warunki są prawdziwe, dodaje liczbę do sumy
            total += num
            
    # Zwraca całkowitą sumę liczb spełniających kryteria
    return total