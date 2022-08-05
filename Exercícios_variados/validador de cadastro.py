nome = str(input("Nome: ")).strip()
idade = int(input("Idade: "))
salario = float(input("Salário: R$"))
sexo = str(input("Sexo ( M ou F): ")).lower()
est = str(input("Estado civil(C - casado, S - Solteiro, V - Viúvo e D-Divorciado): ")).lower()

while len(nome) <= 3:
  nome = str(input("Nome inválido, digite novamente seu nome: ")).strip()

while idade < 0 or idade > 150:
  idade = int(input("Idade inválida, digite novamente a idade: "))

while salario < 0:
  salario = float(input("Salário inválido, digite novamente: R$"))

while sexo != 'm' and sexo != 'f':
  sexo = str(input("Sexo inválido, digite novamente: "))

while est != 'c' and est != 's' and est != 'v' and est != 'd':
  est = str(input("Esta civil inválido, digite novamente: "))

print("Cadastro efetuado com sucesso")



