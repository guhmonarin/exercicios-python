import random

a = input("Primeiro aluno: ")
b = input("Segundo aluno: ")
c = input("Terceiro aluno: ")
d = input("Quarto aluno: ")
lista = [a,b,c,d]
e = random.choice(lista)

print("O nome escolhido foi: {}".format(e))