a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
soma = 0
if a > b:
  for val in range((b+1),a):
    print(val)
    soma+=val

else:
  for val in range((a+1),b):
    print(val)
    soma+=val

print("A soma dos valores do intervalo é {}".format(soma))