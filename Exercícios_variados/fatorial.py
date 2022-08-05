cont = 's'
while cont == 's':
  n = int(input("Digite o numero para calcular o fatorial: "))
  if n >= 0 and n <=16:
    fat = n
    while n > 1:
      n = n-1
      fat = fat*n
  
    print("Fatorial: {}".format(fat))
  else:
    print("Número invalido")

  cont = input("\nDeseja continuar calculando? (S/N): ").lower()

print("\nExit")