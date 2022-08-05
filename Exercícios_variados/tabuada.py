while True:
  s = input("Deseja fazer tabuada? (S/N): ").lower()
  if s == 'n':
    break;
  tabuada = int(input("Montar a tabuada: "))
  comeco = int(input("Começar por: "))
  fim = int(input("Terminar em: "))
  print("-"*50)
  if comeco <= fim:
    print("Vou montar a tabuada do {} começando em {} e terminando em {}:".format(tabuada,comeco,fim))
    for i in range(comeco,fim+1):
      print("{} * {} = {}".format(tabuada,i,(i*tabuada)))
   
  elif fim < comeco:
    print("Valor inválido, digite novamente")

  print("-"*50)