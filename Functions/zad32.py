# Definiuje funkcję 'f', która przyjmuje napis ('palindrome') do sprawdzenia
def f(palindrome):
    # palindrome[::-1] -> tworzy odwróconą kopię napisu (wycinanie/slicing z krokiem -1, czyli od końca do początku)
    # palindrome == ... -> porównuje oryginalny napis z jego odwróconą wersją i zwraca True lub False
    return palindrome == palindrome[::-1]