a =str(input("Digite o seu nome completo: ")).strip()
a = a.split()
b = len(a)-1
print("O seu primeiro nome é: {}".format(a[0]))
print("O seu ultimo nome é: {}".format(a[b]))

