# Definiuje funkcję 'f', która przyjmuje ciąg tekstowy ('name')
def f(name):
    # name.split() -> dzieli tekst na listę pojedynczych słów (domyślnie rozdzielając po spacjach)
    # word[0]      -> dla każdego słowa z tej listy pobiera jego pierwszy znak (indeks 0)
    # "".join(...) -> łączy wszystkie pobrane pierwsze litery w jeden ciągły napis (bez spacji)
    return "".join(word[0] for word in name.split())