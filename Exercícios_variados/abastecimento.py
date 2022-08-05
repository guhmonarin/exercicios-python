litros = int(input("Quantos litros vocês abasteceu? "))
comb = str(input("Qual foi o combustivel? (G-Gasolina ou A-Alcool:"))

if comb == 'A':
  if litros <= 20:
    a = str('Alcool')
    valor = float(litros * 1.90)
    pagar = valor-(valor*0.03)
  else:
    a = str('Alcool')
    valor = float(litros * 1.90)
    pagar = valor-(valor*0.05)

if comb == 'G':
  if litros <= 20:
    a = str('Gasolina')
    valor = float(litros * 2.50)
    pagar = valor-(valor*0.04)
  else:
    a = str('Gasolina')
    valor = float(litros * 2.50)
    pagar = valor-(valor*0.06)

print("Você abasteceu com {}".format(a))
print("Você abasteceu {} litros, e deverá pagar: R${:.2f}".format(litros,pagar))