def input_string(message):
    val = input(message)
    return val

def input_integer(message):
    val = int(input(message))
    return val

def input_real(message):
    val = float(input(message))
    return val

def input_boolean(message):
    val = input(message).strip().lower()
    return val == 'y'