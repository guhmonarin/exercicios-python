nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2)/2
print("-"*50)
if media >= 9 and media < 10:
  print("NOTA DO PRIMEIRO SEMESTRE {:.2f}".format(nota1))
  print("NOTA DO SEGUNDO SEMESTRE: {:.2f}".format(nota2))
  print("MÉDIA: {:.2f}".format(media))
  print("CONCEITO: A")
  print("\nVOCÊ FOI APROVADO")

elif media < 9 and media >=7.5:
  print("NOTA DO PRIMEIRO SEMESTRE {:.2f}".format(nota1))
  print("NOTA DO SEGUNDO SEMESTRE: {:.2f}".format(nota2))
  print("MÉDIA: {:.2f}".format(media))
  print("CONCEITO: B")
  print("\nVOCÊ FOI APROVADO")

elif media <7.5 and media >= 6:
  print("NOTA DO PRIMEIRO SEMESTRE {:.2f}".format(nota1))
  print("NOTA DO SEGUNDO SEMESTRE: {:.2f}".format(nota2))
  print("MÉDIA: {:.2f}".format(media))
  print("CONCEITO: C")
  print("\nVOCÊ FOI APROVADO")

elif media < 6 and media >= 4:
  print("NOTA DO PRIMEIRO SEMESTRE {:.2f}".format(nota1))
  print("NOTA DO SEGUNDO SEMESTRE: {:.2f}".format(nota2))
  print("MÉDIA: {:.2f}".format(media))
  print("CONCEITO: D")
  print("\nVOCÊ FOI REPROVADO")

elif media < 4 and media >= 0:
  print("NOTA DO PRIMEIRO SEMESTRE {:.2f}".format(nota1))
  print("NOTA DO SEGUNDO SEMESTRE: {:.2f}".format(nota2))
  print("MÉDIA: {:.2f}".format(media))
  print("CONCEITO: E")
  print("\nVOCÊ FOI REPROVADO")

else:
  print("NOTAS DIGITAS SÃO INVALIDAS")

print("-"*50)