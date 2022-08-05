def valorPagamento(parcela,n):
    if n == 0:
        valor_pagar = parcela
    if n >= 1:
        multa = parcela*0.03
        juros = parcela*(0.001*n)
        valor_pagar = parcela+multa+juros
    print(f'O valor da parcela é R${valor_pagar:.2f}')
    return valor_pagar

contador = 0
valortotal = 0
while True:

    valor = float(input('Valor da parcela: R$'))
    if valor == 0:
        break;
    dias = int(input('Quantos dias de atraso:'))
    valortotal = valorPagamento(valor,dias)+valortotal
    contador += 1

print('RELATÓRIO DO DIA')
print(f'Foi paga {contador} parcelas!')
print(f'Total valor pago R${valortotal}')