import os

print("ELEIÇÃO 2022")
print("-"*80)
contador=0
cand1=0
cand2=0
cand3=0
cand4=0
nulo=0
branco=0
while True:
  votar = input("Deseja iniciar a votação? (S/N): ").lower()
  if votar == 'n':
    break;
  else:
    os.system('clear') or None
    contador += 1
    print("-"*80)
    print("VOTE:")
    print("-"*80)
    print("1 - Lucas")
    print("2 - Gustavo")
    print("3 - Melissa")
    print("4 - Marilisa")
    print("5 - Voto nulo")
    print("6 - Voto em branco")
    print("-"*80)
    voto = int(input("Escolha a opção: "))

    if voto == 1:
      cand1+=1
    elif voto == 2:
      cand2+=1
    elif voto == 3:
      cand3+=1
    elif voto == 4:
      cand4+=1
    elif voto == 5:
      nulo+=1
    elif voto == 6:
      branco+=1
    os.system('clear') or None

os.system('clear') or None

perc_branco = (branco/contador)*100
perc_nulo = (nulo/contador)*100
print("RESULTADO ELEIÇÃO 2022: ")
print("-"*80)
print("Lucas:           {} votos".format(cand1))
print("Gustavo:         {} votos".format(cand2))
print("Melissa:         {} votos".format(cand3))
print("Marilisa:        {} votos".format(cand4))
print("-"*80)
print("Votos Nulo:      {} votos".format(nulo))
print("Votos em branco: {} votos".format(branco))
print("-"*80)
print("Tivemos {}% de votos brancos".format(perc_branco))
print("Tivemos {}% de votos nulos".format(perc_nulo))