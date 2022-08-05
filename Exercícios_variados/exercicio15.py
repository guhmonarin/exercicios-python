km = float(input("Digite a quantidade de KM que o carro andou: "))
dias = float(input("Digite a quantide de dias que esse carro ficou alugado: "))
pagar=(dias*60)+(km*0.15)

print("Você ficou com o carro por {:.0f} dias e andou {:.0f}KM, com isso você terá que pagar R${:.2f} reais".format(dias, km, pagar))