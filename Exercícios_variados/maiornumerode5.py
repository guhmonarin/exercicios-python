a = int(input("Digite um número 1: "))
b = int(input("Digite um número 2: "))
c = int(input("Digite um número 3: "))
d = int(input("Digite um número 4: "))
e = int(input("Digite um número 5: "))
lista=[a,b,c,d,e]
maior = lista [0]
cont = 0
while cont < len(lista):
  if lista [cont] > maior:
    maior = lista[cont]

  cont+=1

print("O maior número é {}".format(maior))