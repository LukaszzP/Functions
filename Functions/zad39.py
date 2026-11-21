# Definiuje funkcję 'f', która przyjmuje wyrażenie matematyczne jako napis ('expression')
def f(expression):
    # Pobiera pierwszy znak (indeks 0), zamienia go na liczbę całkowitą i zapisuje jako początkowy wynik
    total = int(expression[0])
    
    # Pętla przechodzi po indeksach co 2 kroki (1, 3, 5...), zatrzymując się zawsze na znakach działań (+ lub -)
    for i in range(1, len(expression), 2):
        # Pobiera znak operatora matematycznego spod bieżącego indeksu 'i'
        op = expression[i]
        # Pobiera kolejną cyfrę stojącą tuż za operatorem (indeks i + 1) i zamienia ją na liczbę całkowitą
        num = int(expression[i + 1])
        
        # Jeśli operatorem jest plus, dodaje liczbę do dotychczasowego wyniku
        if op == '+':
            total += num
        # Jeśli operatorem jest minus, odejmuje liczbę od dotychczasowego wyniku
        elif op == '-':
            total -= num
            
    # Zwraca ostateczny wynik obliczeń
    return total