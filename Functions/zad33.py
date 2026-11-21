# Definiuje funkcję 'f', która przyjmuje dowolny ciąg tekstowy ('sentence')
def f(sentence):
    # Wywołuje metodę .replace(), która wyszukuje w tekście każdy znak spacji (" ")
    # i zastępuje go pustym ciągiem znaków (""), czyli go usuwa, a następnie zwraca nowy napis
    return sentence.replace(" ", "")