def positivo_negativo(numero):
    if numero > 0:
        return 'P'
    if numero <= 0:
        return 'N'


a = float(input('Digite um número: '))
print(positivo_negativo(a))
