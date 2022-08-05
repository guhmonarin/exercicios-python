a = int(input("Digite um número de 0 a 9999: "))

unidade =a%10
a = (a-unidade)/10
dezena=a%10
a = (a-dezena)/10
centena=a%10
a = (a-centena)/10
milhar=a

print("Analisando o número {}".format(a))
print("Unidade: {:.0f}".format(unidade))
print("Dezena: {:.0f}".format(dezena))
print("Centena: {:.0f}".format(centena))
print("Milhar: {:.0f}".format(milhar))