from math import pow, sqrt

a = float(input("Comprimento do cateto oposto: "))
b = float(input("Comprimento do cateto adjacente: "))
c = sqrt(pow(a,2)+pow(b,2))

print("A hipotenusa vai medir {:.2f}".format(c))