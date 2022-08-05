def conversao(hora,minuto):
    if hora >= 13 and hora <= 24:
        hora_horario = hora - 12
        print(f'Agora são: {hora_horario:02}:{minuto:02} P.M.')
    
    if hora == 12:
        print(f'Agora são: {hora:02}:{minuto:02} P.M.')
    
    if hora < 12 and hora >= 1:
        print(f'Agora são: {hora:02}:{minuto:02} A.M.')
    
    if hora >= 0 and hora <=1:
        print(f'Agora são: {hora:02}:{minuto:02} A.M.')


while True:

    h = int(input('Digite a hora: '))
    if h == 25:
        break;
        
    m = int(input('Digite o minuto: '))

    conversao(h,m)