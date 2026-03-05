from enum import Enum


class Geschlecht(Enum):
    MAENNLICH = "m"
    WEIBLICH = "w"


class Person:
    def __init__(self, name, geschlecht):
        self.name = name
        self.geschlecht = geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, personalNummer, abteilung):
        super().__init__(name, geschlecht)
        self.personalNummer = personalNummer
        self.abteilung = abteilung
        abteilung.mitarbeiter.append(self)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, personalNummer, abteilung):
        super().__init__(name, geschlecht, personalNummer, abteilung)


class Abteilung:
    def __init__(self, name):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def setLeiter(self, leiter):
        if self.leiter is not None:
            raise ValueError("Es gibt bereits einen Abteilungsleiter.")
        if leiter.abteilung is not self:
            raise ValueError("Leiter muss in dieser Abteilung sein.")
        self.leiter = leiter

    def mitarbeiterAnzahl(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name):
        self.name = name
        self.abteilungen = []

    def addAbteilung(self, abteilung):
        self.abteilungen.append(abteilung)

    def mitarbeiterAnzahl(self):
        return sum(abt.mitarbeiterAnzahl() for abt in self.abteilungen)

    def abteilungsleiterAnzahl(self):
        return sum(1 for abt in self.abteilungen if abt.leiter is not None)

    def abteilungsAnzahl(self):
        return len(self.abteilungen)

    def abteilungMitGroessterStaerke(self):
        if not self.abteilungen:
            return None
        return max(self.abteilungen, key=lambda abt: abt.mitarbeiterAnzahl())

    def geschlechterAnteileProzent(self):
        alle = []
        for abt in self.abteilungen:
            alle.extend(abt.mitarbeiter)

        if len(alle) == 0:
            return {"Frauen": 0.0, "Maenner": 0.0}

        frauen = sum(1 for m in alle if m.geschlecht == Geschlecht.WEIBLICH)
        maenner = sum(1 for m in alle if m.geschlecht == Geschlecht.MAENNLICH)

        gesamt = len(alle)
        return {
            "Frauen": (frauen / gesamt) * 100,
            "Maenner": (maenner / gesamt) * 100,
        }


def main():
    firma = Firma("Tirol Kliniken GmbH")

    it = Abteilung("IT")
    az = Abteilung("Aerzte")
    firma.addAbteilung(it)
    firma.addAbteilung(az)

    Mitarbeiter("Arnout", Geschlecht.MAENNLICH, 1001, it)
    Mitarbeiter("Anna", Geschlecht.WEIBLICH, 1002, it)
    Mitarbeiter("Raphael", Geschlecht.MAENNLICH, 2001, az)

    leiterIt = Abteilungsleiter("Nathan", Geschlecht.MAENNLICH, 9001, it)
    it.setLeiter(leiterIt)

    print(f"Firma: {firma.name}")
    print(f"Abteilungen: {firma.abteilungsAnzahl()}")
    print(f"Mitarbeiter gesamt: {firma.mitarbeiterAnzahl()}")
    print(f"Abteilungsleiter: {firma.abteilungsleiterAnzahl()}")

    groesste = firma.abteilungMitGroessterStaerke()
    if groesste is not None:
        print(
            f"Groesste Abteilung: {groesste.name} "
            f"({groesste.mitarbeiterAnzahl()} Mitarbeiter)"
        )

    anteile = firma.geschlechterAnteileProzent()
    print(f"Frauen: {anteile['Frauen']:.2f}%")
    print(f"Maenner: {anteile['Maenner']:.2f}%")


if __name__ == "__main__":
    main()
