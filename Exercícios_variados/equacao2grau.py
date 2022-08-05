a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
x = 0

if a != 0:
  delta = (b**2)-(4*a*c)

  if delta < 0:
    print("A equação não possui raizes reais")

  elif delta == 0:
    raiz = (-b)/(2*a)
    print("A equação possui apenas uma raiz no valor: {:.2f}".format(raiz))

  elif delta > 0:
    raiz1 = ((-b)+delta)/(2*a)
    raiz2 = ((-b)-delta)/(2*a)
    print("As duas raizes da equação são {:.2f} e {:.2f}".format(raiz1,raiz2))

elif a == 0:
  print("A equação não é do segundo grau")
