continuar = 's'

while continuar == 's':  
  total = 0
  contador = 1
  lista = [0]
  while continuar == 's':
    preco = float(input("Preço do produto {}: R$".format(contador)))
    lista.append(preco)
    total += preco
    contador += 1
    if preco == float(0):
      break;
  contador_lista = 1    
  dinheiro = float(input("Valor recebido: R$"))
  
  print("-"*50)
  print("LOJAS TABAJARAS")
  while contador_lista < contador:
    print("Produto {}: R${:.2f}".format(contador_lista,lista[contador_lista]))
    contador_lista +=1
  print("Total: R${:.2f}".format(total))
  print("Dinheiro: R${:.2f}".format(dinheiro))
  print("Troco: R${:.2f}".format(dinheiro-total))
  print("-"*50)

  continuar = str(input("Deseja fazer outra venda? (S/N): ")).lower()

print("SAIR DO PROGRAMA")