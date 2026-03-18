import random

class Knoten:
    def __init__(self, data):
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def am_ende_hinzufuegen(self, value):
        new_node = Knoten(value)
        if not self.head:
            self.head = new_node
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = new_node
        self._length += 1

    def ausgabe_laenge(self):

        return self._length

    def alle_elemente_ausgeben(self):
        now = self.head
        elements = []
        while now:
            elements.append(str(now.data))
            now = now.next
        print("Liste: " + " -> ".join(elements))

    def __iter__(self):
        self._now_iter = self.head
        return self

    def __next__(self):
        if self._now_iter is None:
            raise StopIteration
        else:
            data = self._now_iter.data
            self._now_iter = self._now_iter.next
            return data

if __name__ == "__main__":
    meine_liste = LinkedList()

    print("Liste mit Zufallszahlen befüllen")
    for i in range(5):
        zufallszahl = random.randint(1, 100)
        meine_liste.am_ende_hinzufuegen(zufallszahl)

    print(f"Länge der Datenstruktur: {meine_liste.ausgabe_laenge()}")

    meine_liste.alle_elemente_ausgeben()

    print("Iteration über die Liste:")
    for wert in meine_liste:
        print(f"Element: {wert}")