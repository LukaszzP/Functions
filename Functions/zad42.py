# Definiuje funkcję 'f', która przyjmuje 4-cyfrowy kod produktu jako ciąg tekstowy ('product_code')
def f(product_code):
    # product_code[:3] -> wycina pierwsze trzy znaki kodu (indeksy 0, 1, 2)
    # int(d)           -> zamienia każdy z tych trzech znaków na liczbę całkowitą
    # sum(...)         -> sumuje te trzy cyfry i zapisuje wynik w zmiennej 'digits_sum'
    digits_sum = sum(int(d) for d in product_code[:3])
    
    # Pobiera czwarty znak kodu (indeks 3) i zamienia go na liczbę całkowitą (cyfrę kontrolną)
    control_digit = int(product_code[3])
    
    # Oblicza resztę z dzielenia sumy pierwszych trzech cyfr przez 7 (digits_sum % 7)
    # i porównuje ją z cyfrą kontrolną; zwraca True, jeśli są równe, lub False, jeśli się różnią
    return (digits_sum % 7) == control_digit