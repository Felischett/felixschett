names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

combine = zip(names, ages, scores)

f = filter(lambda eintrag: eintrag[1] >= 3 and eintrag[2] >= 80, combine)
#Lambda wird nur an einer stelle verwendet!
#nur ein return wert
#Anonyme Funktionen
#Vorkompeliert (nicht ganz klar ob schneller)
#Kapselung von Logik

ergebnis = map(lambda eintrag: {"names": eintrag[0], "alter": eintrag[1], "punkte": eintrag[2]}, f)

print(list(ergebnis))
