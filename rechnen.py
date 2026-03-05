# rechner.py

def addiere(a, b):
    return a + b

def dividiere(a, b):
    if b == 0:
        raise ValueError("Division durch 0 nicht erlaubt")
    return a / b
