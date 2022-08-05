n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1


if n == 1 or n == 2:
  print("1")
else:
  cont = 3
  while cont <= n:
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    cont += 1

print(termo)