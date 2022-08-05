a = int(input("Digite o número 1: "))
b = int(input("Digite o número 2: "))
c = int(input("Digite o número 3: "))
d = int(input("Digite o número 4: "))
e = int(input("Digite o número 5: "))
f = int(input("Digite o número 6: "))
g = int(input("Digite o número 7: "))
h = int(input("Digite o número 8: "))
i = int(input("Digite o número 9: "))
j = int(input("Digite o número 10: "))

lista=[a,b,c,d,e,f,g,h,i,j]
cont = 0
con = 0
par = 0
impar = 0

while cont < len(lista):
  if lista[cont]%2 == 0:
    par += 1
   
  cont += 1

while con < len(lista):
  if lista[con]%2 != 0:
    impar += 1
   
  con += 1

print("A sequencia tem {} números pares e {} números impares".format(par,impar))