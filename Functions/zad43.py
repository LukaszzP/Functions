# Definiuje funkcję 'f', która przyjmuje ciąg znaków ('dice') reprezentujący kolejne rzuty kostką
def f(dice):
    # Przechowuje długość najdłuższej znalezionej dotychczas serii (na początku 1)
    max_streak = 1
    # Liczy długość aktualnie trwającej serii takich samych rzutów (na początku 1)
    current_streak = 1
    # Zapamiętuje cyfrę, która utworzyła najdłuższą serię (domyślnie pierwszy rzut z brzegu)
    best_digit = dice[0]
    
    # Pętla przechodzi po indeksach od drugiego znaku (indeks 1) do końca napisu
    for i in range(1, len(dice)):
        # Porównuje obecny rzut (dice[i]) z poprzednim rzutem (dice[i - 1])
        if dice[i] == dice[i - 1]:
            # Jeśli wypadło to samo oczko co poprzednio, wydłuża bieżącą serię o 1
            current_streak += 1
            # Sprawdza, czy bieżąca seria pobiła dotychczasowy rekord długości
            if current_streak > max_streak:
                max_streak = current_streak  # Aktualizuje rekord długości serii
                best_digit = dice[i]         # Zapisuje cyfrę, która osiągnęła ten rekord
        else:
            # Jeśli wypadło inne oczko niż poprzednio, resetuje licznik bieżącej serii z powrotem do 1
            current_streak = 1
            
    # Zamienia zapamiętany znak zwycięskiej cyfry na liczbę całkowitą (int) i zwraca wynik
    return int(best_digit)