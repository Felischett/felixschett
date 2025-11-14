a = 201
b = 200
i = 1

# if, else
if b > a:
  print("b größer als a")
else:
    print("a größer als b")

# elif
if b > a:
  print("b größer als a")
elif a == b:
  print("a & b sind gleich")
else:
  print("a größer als b")

# try, except
try:
  print(c)
except:
    print("Variable c ist nicht definiert")
else:
    print("Keine Fehler")
finally:
    print("Fertig")

# while, break
while i < 6:
  print(i)
  i += 1
  if i == 3:
      break

# for, pass
fruechte = ["Apfel", "Banane", "Erdbeere"]
for x in fruechte:
  print(x)
pass    # falls leer, dann pass (kein Fehler)











