def somaImposto(taxaimposto, custo):
    custo += (taxaimposto*custo)/100
    return custo


imposto = float(input('Digite o imposto de um produto: '))
custo = float(input('Digite o custo do produto: R$'))

custo = somaImposto(imposto,custo)

print(f'O custo do produto é R$ {custo:.2f}')