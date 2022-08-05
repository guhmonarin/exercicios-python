nome = str(input("Digite o seu nome completo: ")).strip()

print("Analisando seu nome...")
print("Seu nome em MAIÚSCULAS é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
nome=nome.split()

print("Seu nome tem ao todo {} letras".format(len(''.join(nome))))

nome=nome[0]

print("Seu primeiro nome é {} e ele tem {} letras".format(nome,len(nome)))

