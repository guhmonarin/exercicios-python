from math import inf

alto = 0
cod_alto = 0

baixo = inf
cod_baixo = 0

gordo = 0
cod_gordo = 0

magro = inf
cod_magro = 0

soma_peso = 0
soma_altura = 0

contador = 0
print("SISTEMA PARA ACADEMIAS")
while True:
  print("-"*100)
  codigo = int(input("Digite o seu código: "))
  if codigo == 0:
    break;
  altura = float(input("Digite sua altura: "))
  
  if altura > alto:
    alto = altura
    cod_alto = codigo
    
  elif altura < baixo:
    baixo = altura
    cod_baixo = codigo
    
  peso = float(input("Digite o seu peso: "))

  if peso > gordo:
    gordo = peso
    cod_gordo = codigo

  elif peso < magro:
    magro = peso
    cod_magro = codigo

  
  contador += 1
  soma_peso+=peso
  soma_altura+=altura


media_peso = soma_peso/contador
media_altura = soma_altura/contador

print("-"*100)
print("O cliente {} é o mais alto com {} metros.".format(cod_alto,alto))
print("O cliente {} é o mais baixo com {} metros.".format(cod_baixo,baixo))
print("O cliente {} é o mais gordo com {} kilos.".format(cod_gordo,gordo))
print("O cliente {} é o mais magro com {} kilos.".format(cod_magro,magro))
print("\nA média das alturas foi {} kilos".format(media_peso))
print("A media de peso foi {} kilos".format(media_altura))
print("-"*100)