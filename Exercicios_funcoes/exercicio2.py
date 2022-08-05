x = int(input('Digite um número: '))

def numero(n):
    print('')
    for i in range(n):
        print(f'{i+1} ', end='')


for n in range(x):
    n += 1
    numero(n)