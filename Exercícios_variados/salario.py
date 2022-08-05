import tkinter as tk

window = tk.Tk()
salario = float(input("Digite o sálario do colaborador: R$"))
perc = 0
reaj = 0
sal_novo = 0

if salario <= 280 and salario > 0:
  perc = 20
  reaj = salario*0.20
  sal_novo=salario+(salario*0.20)

elif salario > 280 and salario <= 700:
  perc = 15
  reaj = salario*0.15
  sal_novo=salario+(salario*0.15)
elif salario > 700 and salario <= 1500:
  perc = 10
  reaj = salario*0.10
  sal_novo=salario+(salario*0.10)
elif salario > 1500:
  perc = 5
  reaj = salario*0.05
  sal_novo=salario+(salario*0.05)
else:
  salario = 0
  print("\nVALOR DIGITADO É INVÁLIDO")


print("-"*50)
print("SALÁRIO ATUAL: R${:.2f}".format(salario))
print("PERCENTUAL APLICADO:{:.0f}%".format(perc))
print("VALOR DO AUMENTO: R${:.2f}".format(reaj))
print("NOVO SALÁRIO: R${:.2f}".format(sal_novo))
print("-"*50)

window.mainloop()