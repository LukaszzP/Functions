# Definiuje funkcję 'f', która przyjmuje hasło jako ciąg tekstowy ('password')
def f(password):
    # Sprawdza jednocześnie dwa warunki połączone operatorem 'and':
    # 1. len(password) >= 6 -> sprawdza, czy długość hasła wynosi co najmniej 6 znaków
    # 2. len(set(password)) == len(password) -> zamienia napis na zbiór (set), który automatycznie usuwa duplikaty.
    #    Jeśli długość zbioru jest równa długości oryginalnego hasła, oznacza to, że żaden znak się nie powtórzył.
    return len(password) >= 6 and len(set(password)) == len(password)