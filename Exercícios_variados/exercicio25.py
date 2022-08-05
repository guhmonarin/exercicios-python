a = str(input("Qual o seu nome completo? ")).strip()
a = a.lower()
print("Seu nome tem silva? {}".format(a.find('silva')>0))