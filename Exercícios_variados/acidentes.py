from math import inf

maior_acidente = 0
codigo_maior = 0

menor_acidente = inf
codigo_menor = 0
cont = 1
soma_veiculo=0
soma_acidente = 0
cont_acidente = 0

while cont <= 5:
  codigo = int(input("Digite o código da cidade {}: ".format(cont)))
  veiculo = int(input("Digite o número de veiculos de passeio: "))
  soma_veiculo += veiculo
  acidente = int(input("Digite o número de acidentes de trânsito com vítimas: "))
  if acidente < 2000:
    soma_acidente += acidente
    cont_acidente += 1
  print("-"*70)
  if acidente > maior_acidente:
    codigo_maior = codigo
    maior_acidente = acidente

  if acidente < menor_acidente:
    codigo_menor = codigo
    menor_acidente = acidente

  cont += 1

media = soma_veiculo/5
media_acidente = soma_acidente/cont_acidente

print("O maior indice de acidentes é da cidade {} com {} acidentes!".format(codigo_maior,maior_acidente))
print("O menor indice de acidentes é da cidade {} com {} acidentes!".format(codigo_menor,menor_acidente))
print("A media de veiculos na 5 cidades juntas são: {}".format(media))
print("A media de acidentes com menos de 2000 é: {}".format(media_acidente))