# Definiuje funkcję 'f', która przyjmuje numer szukanej liczby pierwszej ('n')
def f(n):
    # Licznik znalezionych dotychczas liczb pierwszych (na początku 0)
    count = 0
    # Aktualnie sprawdzana liczba (zaczyna od 1, aby w pierwszym kroku pętli przejść do 2)
    candidate = 1
    
    # Pętla główna działa dopóki nie znajdziemy 'n' liczb pierwszych
    while count < n:
        # Przechodzi do kolejnej liczby do sprawdzenia (2, 3, 4, 5...)
        candidate += 1
        # Zakłada wstępnie, że sprawdzana liczba jest pierwsza
        is_prime = True
        
        # Pętla sprawdza dzielniki od 2 do pierwiastka kwadratowego z badanej liczby (candidate ** 0.5)
        # (wystarczy sprawdzać do pierwiastka, ponieważ większe dzielniki miałyby już parę mniejszą od pierwiastka)
        for i in range(2, int(candidate ** 0.5) + 1):
            # Jeśli 'candidate' dzieli się bez reszty przez 'i', to nie jest liczbą pierwszą
            if candidate % i == 0:
                is_prime = False  # Oznacza liczbę jako złożoną (niepierwszą)
                break             # Przerywa wewnętrzną pętlę, bo dalsze sprawdzanie nie ma sensu
                
        # Jeśli po sprawdzeniu wszystkich dzielników flaga 'is_prime' nadal ma wartość True...
        if is_prime:
            # ...zwiększa licznik znalezionych liczb pierwszych o 1
            count += 1
            
    # Gdy pętla while znajdzie n-tą liczbę pierwszą, funkcja zwraca jej wartość
    return candidate