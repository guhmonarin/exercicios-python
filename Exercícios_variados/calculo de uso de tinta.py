from math import ceil,floor

a = float(input("Digite a altura da parede: "))
l = float(input("Digite a largura da parede: "))
area = a * l
litros = area / 6

qtde_lata = ceil(litros / 18)
pre_lata = qtde_lata * 80

qtde_gal = ceil(litros/3.6)
pre_gal = qtde_gal*25

print("\nVocê gastará {:.2f} litros ".format(litros))
print("\nSe você comprar lata de 18 litros, precisará comprar {} lata(s), que custará R${:.2f}".format(qtde_lata, pre_lata))
print("Se você comprar galões de 3.6 litros, precisára comprar {} galão(s), que custará R${:.2f}".format(qtde_gal,pre_gal))
print("A forma mais economica para você será se: ")

lata=floor(litros/18)
preco_lata=lata*80
litros_restante = litros%18
qtde_gal_novo=ceil(litros_restante/3.6)
preco_galao=(qtde_gal_novo*25)+preco_lata

if litros_restante <= 10.8:
  print("Você comprar {} lata(s) de 18 litros e {} galão (s) de 3.6 litros e irá gastar: R${:.2f}".format(lata,qtde_gal_novo,preco_galao))
else:
  print("Você comprar {} lata(s) de 18 litros e irá gastar: R${:.2f}".format(lata + 1 ,(lata+1)*80))