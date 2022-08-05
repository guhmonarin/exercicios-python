sal=float(input("Digite qual é o salário do funcionário: R$"))
reajuste=sal+(sal*0.15)

print("Um funcionário que ganhava R${:.2f}, com 15% de aumento , passa a ganhar R${:.2f}".format(sal,reajuste))