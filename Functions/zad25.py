# Definiuje funkcję 'f', która przyjmuje początek ('x') i koniec ('y') przedziału liczbowego
def f(x, y):
    # Zmienna licznika przechowująca liczbę znalezionych liczb (na początku 0)
    count = 0
    
    # Pętla przechodzi po wszystkich liczbach całkowitych od 'x' do 'y' włącznie
    # (dodajemy + 1 do 'y', ponieważ funkcja range() domyślnie pomija górną granicę)
    for num in range(x, y + 1):
        # Sprawdza jednocześnie dwa warunki:
        # 1. num < 0      -> liczba jest mniejsza od zera (czyli ujemna)
        # 2. num % 2 == 0 -> reszta z dzielenia liczby przez 2 wynosi 0 (czyli liczba jest parzysta)
        if num < 0 and num % 2 == 0:
            count += 1  # Jeśli oba warunki są spełnione, zwiększa licznik o 1
            
    # Zwraca całkowitą liczbę znalezionych ujemnych liczb parzystych
    return count