import os
print("GABARITO DA PROVA 2022")
gabarito = []
contador = 1
aluno = 1
while True:  
  pergunta=input("Resposta da questao {}: ".format(contador)).lower()
  if pergunta == '0':
    break;
  else:
    contador+=1
    gabarito.append(pergunta)

os.system('clear') or None

print("PROVA 2022")
aluno = 0
total = []
while True:
  os.system('clear') or None
  comecar = input("Iniciar a prova? ").lower()
  if comecar == 'n':
    break;  
  else:
    
    aluno += 1
    cont = 0
    acerto = 0
    valor = 0
    while cont < (contador-1):
      cont += 1
      resposta = input("Resposa da questão {}".format(cont)).lower()
      if resposta == gabarito[valor]:  
        acerto += 1
      valor += 1
    total.append(acerto)
    
os.system('clear') or None

media = sum(total)/aluno
print("RESULTADO")
print("-"*80)
print("O maior número de acertos foi {}".format(max(total)))
print("O menor número de acertos foi {}".format(min(total)))
print("O numero de alunos que usou o sistema foi {}.".format(aluno))
print("A media de acerto foi {:.0f}".format(media))
print("-"*80)