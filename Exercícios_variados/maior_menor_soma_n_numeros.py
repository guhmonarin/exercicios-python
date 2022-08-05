from math import inf

n = int(input("Digite a quantidade de números: "))
cont = 0
maior=0
soma=0
menor=inf

while cont < n:
  x = int(input("Digite o número: "))
  if x >= 0 and x <=1000:
    soma+=x
    cont+=1
    if x > maior:
      maior = x
    if x < menor:
      menor = x
  else:
    print("\nDigite o valor entre 0 e 1000\n")


print("\nO maior valor é: {}".format(maior))
print("O menor valor é: {}".format(menor))
print("A soma dos valores são: {}".format(soma))