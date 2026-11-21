# Definiuje funkcję rekurencyjną 'sum_natural', która przyjmuje liczbę całkowitą 'n'
def sum_natural(n):
    # Warunek bazowy (stopu): jeśli 'n' jest równe 1 (lub mniejsze), funkcja kończy rekurencję
    # i zwraca bezpośrednio wartość 'n' (np. dla n=1 zwraca 1)
    if n <= 1:
        return n
        
    # Krok rekurencyjny: dodaje bieżącą liczbę 'n' do sumy wszystkich poprzednich liczb od 1 do (n - 1)
    return n + sum_natural(n - 1)

# Wywołuje funkcję dla n = 10 i wypisuje wynik na ekranie ("Sum of natural numbers <1, 10>: 55")
print("Sum of natural numbers <1, 10>:", sum_natural(10))