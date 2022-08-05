conf = 's'

while conf == 's':
  a = int(input("Qual o número da população A? "))
  taxa_a = float(input("Qual a taxa de crescimento da população A(%): "))
  b = int(input("Qual o número da população B? "))
  taxa_b = float(input("Qual a taxa de crescimento da população B(%): "))
  taxa_a = taxa_a/100
  taxa_b = taxa_b/100
  count = 0

  while a < 0:
    a = int(input("Número invalido, qual o número da população A? "))

  while taxa_a < 0:
    taxa_a = float(input("Taxa invalida, qual a taxa de crescimento da população A(%): "))

  while b < 0:
    b = int(input("Número invalido, qual o número da população B? "))

  while taxa_b < 0:
    taxa_b = float(input("Taxa invalida, qual a taxa de crescimento da população B(%): "))


  while a < b:
    a += a*taxa_a
    b += b*taxa_b
    count += 1

  print("\nO país A levará {} anos para ultrapassar o país B".format(count))
  conf=str(input("\nDeseja colocar outra informação? S/N: ")).lower()
  print("\n")

print("Sair do sistema")