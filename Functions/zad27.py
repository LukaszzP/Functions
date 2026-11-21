# Definiuje funkcję 'f', która przyjmuje liczbę całkowitą 'n' (określającą liczbę gwiazdek)
def f(n):
    # ["*"] * n     -> tworzy listę zawierającą znak "*" powtórzony 'n' razy (np. dla n=3: ["*", "*", "*"])
    # "/".join(...) -> łączy wszystkie elementy tej listy w jeden napis, wstawiając między nie znak "/"
    return "/".join(["*"] * n)