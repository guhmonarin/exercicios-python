a = int(input("Digite um número 1: "))
b = int(input("Digite um número 2: "))
c = int(input("Digite um número 3: "))
d = int(input("Digite um número 4: "))
e = int(input("Digite um número 5: "))
lista=[a,b,c,d,e]
soma = 0
cont = 0
while cont < len(lista):
  soma += lista[cont]
  cont+=1

media = soma/len(lista)
print("\nA soma dos número são: {}".format(soma))
print("\nA média dos números são: {}".format(media))