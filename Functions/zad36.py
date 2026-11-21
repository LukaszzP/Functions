# Definiuje funkcję 'f', która przyjmuje trzy liczby jako argumenty: number1, number2 oraz number3
def f(number1, number2, number3):
    # max(...) -> znajduje największą wartość spośród trzech podanych liczb
    # min(...) -> znajduje najmniejszą wartość spośród trzech podanych liczb
    # Odejmuje najmniejszą wartość od największej i zwraca wynik
    return max(number1, number2, number3) - min(number1, number2, number3)