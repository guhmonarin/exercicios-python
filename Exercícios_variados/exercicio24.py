a = str(input("Digite qual cidade você nasceu: ")).strip()
a = a.lower()
a = a.split()
a = a[0]
if a == 'santo':
    print("Verdadeiro")
else:
    print("Falso")

