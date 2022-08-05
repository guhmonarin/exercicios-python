from math import ceil,floor

arquivo=float(input("Qual é o tamanho do arquivo em mb: "))
link=float(input("Qual a velocidade da sua internet: "))

mbs = link/8
segundos = ceil(arquivo / mbs)
minutos = segundos/60
diferenca = segundos%60
if diferenca == 0:
    print("O arquivo irá demorar {} minutos para ser baixado".format(minutos))
else:
  resto=ceil((diferenca*60)/100)
  min=floor(minutos)
  print("O arquivo irá demorar {} minutos e {} segundos".format(min,resto))
