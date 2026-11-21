# Definiuje funkcję 'f', która przyjmuje dowolny ciąg tekstowy ('text')
def f(text):
    # Metoda .join() traktuje napis 'text' jako zbiór pojedynczych znaków
    # i łączy je w jeden nowy napis, wstawiając pomiędzy każdy znak myślnik ("-")
    return "-".join(text)