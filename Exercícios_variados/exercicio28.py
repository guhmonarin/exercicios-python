from random import randint
a = randint(1,5)
b = int(input("Adivinhe um número entre 1 e 5: "))

if a == b:
    print("Parábens vocês acertou o número")
else:
    print("Você errou o número, tenta novamente")
