from math import cos, sin, tan, radians
a = float(input("Digite o angulo que você deseja: "))
b = radians(a)

print("O ângulo de {} tem o seno de {:.2f}".format(a,sin(b)))
print("O ângulo de {} tem o cosseno de {:.2f}".format(a,cos(b)))
print("O ângulo de {} tem a tangente de {:.2f}".format(a,tan(b)))