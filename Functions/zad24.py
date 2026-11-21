# Definiuje funkcję 'f', która przyjmuje liczbę ('number') oraz flagę logiczną ('even': True lub False)
def f(number, even):
    # Zmienna przechowująca sumę pasujących cyfr (na początku 0)
    total = 0
    
    # abs(number) -> usuwa ewentualny znak minus z liczby ujemnej
    # str(...) -> zamienia liczbę na tekst, aby pętla mogła przejść po każdym pojedynczym znaku ('ch')
    for ch in str(abs(number)):
        # Zamienia pojedynczy znak z powrotem na liczbę całkowitą (cyfrę od 0 do 9)
        d = int(ch)
        
        # Sprawdza pierwszy przypadek: czy mamy szukać cyfr parzystych (even == True)
        # ORAZ czy reszta z dzielenia cyfry przez 2 wynosi 0 (czyli cyfra jest parzysta)
        if even and d % 2 == 0:
            total += d  # Dodaje parzystą cyfrę do sumy
            
        # Sprawdza drugi przypadek: czy mamy szukać cyfr nieparzystych (not even, czyli even == False)
        # ORAZ czy reszta z dzielenia cyfry przez 2 jest różna od 0 (czyli cyfra jest nieparzysta)
        elif not even and d % 2 != 0:
            total += d  # Dodaje nieparzystą cyfrę do sumy
            
    # Zwraca obliczoną sumę odpowiednich cyfr
    return total