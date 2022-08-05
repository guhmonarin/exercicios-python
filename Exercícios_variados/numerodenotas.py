saque = int(input("Digite o valor que será sacado: R$"))

if saque >= 10 and saque <=600:
  cem = int(saque/100)
  a = saque%100

  ciq = int(a/50)
  b = a%50

  dez = int(b/10)
  c = b%10

  cinco = int(c/5)
  d = c%5

else:
  print("O valor digitado é invalido")

print("Para sacar a quantia de {} reais, o programa fornece {} nota(s) de 100, {} de 50, {} de 10, {} de 5 e {} nota(s) de 1;".format(saque,cem,ciq,dez,cinco,d))