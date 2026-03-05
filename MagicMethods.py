class Auto:
    def __init__(self, ps: int):
        if not isinstance(ps, int):
            raise TypeError("ps muss ein int sein.")
        if ps < 0:
            raise ValueError("ps darf nicht negativ sein.")
        self.ps = ps

    def _ensure_auto(other, op_name: str):
        if not isinstance(other, Auto):
            raise TypeError(f"{op_name} ist nur zwischen Auto-Objekten erlaubt (bekommen: {type(other).__name__}).")

    def __len__(self) -> int:
        return self.ps

    def __add__(self, other):
        Auto._ensure_auto(other, "Addition")
        return self.ps + other.ps

    def __sub__(self, other):
        Auto._ensure_auto(other, "Subtraktion")
        return self.ps - other.ps

    def __mul__(self, other):
        Auto._ensure_auto(other, "Multiplikation")
        return self.ps * other.ps

    def __eq__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps == other.ps

    def __lt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps < other.ps

    def __gt__(self, other):
        if not isinstance(other, Auto):
            return NotImplemented
        return self.ps > other.ps

    def __repr__(self) -> str:
        return f"Auto(ps={self.ps})"


if __name__ == "__main__":
    a1 = Auto(50)
    a2 = Auto(60)
    a3 = Auto(50)

    print("len(a1) =", len(a1))

    print("a1 + a2 =", a1 + a2)

    print("a2 - a1 =", a2 - a1)

    print("a1 * a2 =", a1 * a2)

    print("a1 == a2 ->", a1 == a2)
    print("a1 == a3 ->", a1 == a3)

    print("a1 < a2 ->", a1 < a2)

    print("a2 > a1 ->", a2 > a1)

    try:
        print(a1 + 5)
    except TypeError as e:
        print("Fehler (a1 + 5):", e)

    try:
        print(a1 - "Auto")
    except TypeError as e:
        print("Fehler (a1 - 'Auto'):", e)

    try:
        print(a1 * None)
    except TypeError as e:
        print("Fehler (a1 * None):", e)