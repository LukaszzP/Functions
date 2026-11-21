# Definiuje funkcję 'f', która przyjmuje napis (ciąg znaków '+' i '-') z detektora ruchu
def f(detector):
    # Zmienna śledząca aktualną liczbę osób w pomieszczeniu (na początku 0)
    people = 0
    
    # Pętla przechodzi kolejno po każdym pojedynczym zdarzeniu (znaku) w napisie 'detector'
    for event in detector:
        # Jeśli zarejestrowano wejście osoby ('+')...
        if event == '+':
            # ...zwiększa liczbę osób w pomieszczeniu o 1
            people += 1
            # Sprawdza, czy w tym momencie w środku są już 3 lub więcej osób
            if people >= 3:
                # Jeśli tak, funkcja natychmiast kończy działanie i zwraca True
                return True
        # W przeciwnym razie, jeśli zarejestrowano wyjście osoby ('-')...
        elif event == '-':
            # ...zmniejsza liczbę osób w pomieszczeniu o 1
            people -= 1
            
    # Jeśli pętla przeanalizowała wszystkie zdarzenia i liczba osób ani razu nie osiągnęła 3, zwraca False
    return False