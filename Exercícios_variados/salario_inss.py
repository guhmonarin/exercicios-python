valor = float(input("Qual o valor da sua hora: R$"))
horas = float(input("Quantas horas você trabalha por mês? "))

salario = valor*horas
ir = 0
inss = 0
fgts = salario*0.11
descontos = 0
sal_liq = 0
irs = 0

if salario <= 900:
  inss = salario*0.10
  descontos = inss+ir
  sal_liq = salario-descontos
elif salario <= 1500 and salario > 900:
  ir = salario*0.05
  irs = 5
  inss = salario*0.10
  descontos = inss+ir
  sal_liq = salario-descontos
elif salario <= 2500 and salario > 1500:
  ir = salario*0.10
  irs = 10
  inss = salario*0.10
  descontos = inss+ir
  sal_liq = salario-descontos
elif salario > 2500:
  ir = salario*0.20
  irs = 20
  inss = salario*0.10
  descontos = inss+ir
  sal_liq = salario-descontos

print("Salário bruto: {} * R${:.2f}          :R${:.2f}".format(horas,valor,salario))
print("(-) IR {}%                            :R${:.2f}".format(irs,ir))
print("(-) INSS 10%                          :R${:.2f}".format(inss))
print("FGTS 11%                              :R${:.2f}".format(fgts))
print("Total de descontos                    :R${:.2f}".format(descontos))
print("Salário Liquido                       :R${:.2f}".format(sal_liq))