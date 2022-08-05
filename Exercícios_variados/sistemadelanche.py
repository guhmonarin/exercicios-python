import os

itens = ['Cachorro Quente','Bauru simples','Bauru com ovo','Hambúrguer','Cheeseburguer','Refrigerante']
codigos = [100,101,102,103,104,105]
preco = [1.20,1.30,1.50,1.20,1.30,1.00]
faturamento = 0
pedido = 0
cont = 's'
while cont == 's':
  itens1 = []
  codigos1 = []
  preco1 = []
  valor = []
  quantidades = []
  pedido+=1
  while True:
    codigo = int(input("\nCódigo: "))
    if codigo == 0:
      break;
    elif codigo not in codigos:
      print("Código inválido, digite codigo novamente: ")
    else:
      quantidade = int(input("Quantidade: "))
      indice = codigos.index(codigo)
      valor_item=quantidade*preco[indice]
      itens1.append(itens[indice])
      codigos1.append(codigo)
      preco1.append(preco[indice])
      valor.append(valor_item)
      quantidades.append(quantidade)

  print("-"*80)
  print("Pedido: {}".format(pedido))
  print("-"*80)
  print("Código Item            Quantidade       Unitário        Total")

  for i in range(len(codigos1)):
  
    print("{:.0f}".format(codigos1[i]),end='    ')
    print("{:16}".format(itens1[i]),end='')
    print("{:10}".format(quantidades[i]),end='       ')
    print("R${:6.2f}".format(preco1[i]),end='      ')
    print("R${:5.2f}".format(valor[i]))
    
  print("-"*80)
  print("\nTotal: R${:.2f}".format(sum(valor)))
  dinheiro = float(input("Dinheiro: R$"))
  troco = dinheiro - sum(valor)
  print("Troco: R${:.2f}".format(troco))
  print("-"*80)
  faturamento+=sum(valor)
  cont = str(input("Deseja fazer novo pedido? ")).lower()
  
  os.system('cls') or None
  
print("\nTotal de pedidos do dia: {}".format(pedido))
print("Faturamento total do dia: R${:.2f}".format(faturamento))