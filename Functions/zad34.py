# Definiuje funkcję 'f', która przyjmuje liczbę całkowitą ('number')
def f(number):
    # abs(number) -> usuwa ewentualny znak minus z liczby ujemnej
    # str(...)    -> zamienia liczbę na napis i zapisuje w zmiennej 's', aby można było badać pojedyncze cyfry
    s = str(abs(number))
    
    # Zmienna przechowująca sumę powtarzających się cyfr (na początku 0)
    total = 0
    
    # Pętla przechodzi kolejno po każdym znaku ('ch') w napisie 's'
    for ch in s:
        # Sprawdza, ile razy bieżąca cyfra ('ch') występuje w całym napisie 's'.
        # Jeśli występuje częściej niż 1 raz (czyli się powtarza)...
        if s.count(ch) > 1:
            # ...zamienia ten znak z powrotem na liczbę całkowitą (int) i dodaje do sumy
            total += int(ch)
            
    # Zwraca całkowitą sumę wszystkich powtarzających się cyfr
    return total