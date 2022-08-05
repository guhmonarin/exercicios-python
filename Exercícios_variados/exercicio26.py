a = str(input("Digite uma frase: ")).strip()
a = a.lower()

print("A letra A aparece {} vezes na frase.".format(a.count('a')))
print("A primeira letra A apareceu na posição {}".format(a.find('a')+1))
print("A última letra A apareceu na posição {}".format(a.rfind('a')+1))