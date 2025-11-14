# Dieses Programm zeigt Beispiele für List-, Dict- und Set-Comprehensions.
# Es erstellt eine Liste mit Quadratzahlen, ein Dictionary mit Zahlen und ihren Quadraten
# sowie ein Set mit einzigartigen Buchstaben aus einem Text.

def list():
    quadrate = []
    for x in range(10):
        quadrate.append(x**2)
    print(quadrate)

#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def dict():
    quadrate_dict = {x: x**2 for x in range(5)}
    print(quadrate_dict)

#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

def set():
    letter = {letter for letter in "ThisIsATest"}
    print(letter)

#{'A', 't', 'I', 's', 'T', 'e', 'i', 'h'}

def main():
    list()
    dict()
    set()

if __name__ == "__main__":
  main()

# Bilde mit comprehension eine funktionalität von set abbilden
# Mach eine Dict Comprehension wo als ergebnis raus kommt, schlüssel alle chars aus dem Englischen Alphabet, 0-anzahl der chars


# a = 2
# b = 3

# a/b gibt echte division mit Kommazahlenzurück
# 0.6666666666

# a//b rundet das Ergebnis auf die nächste unterere ganze Zahl ab
# 0

# Listen sind Mutable / Primitive Datentypen sind immutable
