# Definiuje funkcję 'f', która przyjmuje kwotę do zapłaty ('amount_to_pay')
def f(amount_to_pay):
    # Zmienna przechowująca łączną liczbę zużytych monet (na początku 0)
    coins = 0
    
    # Pętla przechodzi kolejno przez dostępne nominały monet od największego do najmniejszego: 5, potem 2, na końcu 1
    for coin in (5, 2, 1):
        # Dzielenie całkowite (//) sprawdza, ile pełnych monet danego nominału zmieści się w pozostałej kwocie
        # i dodaje tę liczbę do ogólnego licznika monet
        coins += amount_to_pay // coin
        
        # Operator %= (reszta z dzielenia) aktualizuje kwotę do zapłaty o to, co zostało po wydaniu tych monet
        amount_to_pay %= coin
        
    # Zwraca całkowitą, najmniejszą możliwą liczbę monet
    return coins