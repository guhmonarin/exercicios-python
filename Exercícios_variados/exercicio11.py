from re import A


l=float(input("Digite a largura da parede em metros: "))
a=float(input("Digite a altura da parede em metros: "))
area=l*a
tinta=area/2
print("Sua parede tem a dimensao de {:.2f}x{:.2f} e sua área é de {:.2f} m²".format(l,a,area))
print("Neste caso você precisará comprar {} litros de tinta".format(tinta))
print("-"*50)