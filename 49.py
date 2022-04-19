hor = int(input("Informe a atual hora: "))
minu = int(input("Informe o atual minuto: "))
seg = int(input("Informe o atual segundo: "))
durh = int(input("Informe as horas de duração do evento: "))
durm = int(input("Informe os minutos de duração do evento(Acompanha as horas inseridas anteriormente): "))
durs = int(input("Informe os segundos de duração do evento(Acompanha as horas e minutos inseridos anteriormente): "))
horenc = hor + durh
minuenc = minu + durm
segenc = seg + durs
if hor >= 24 or minu >= 60 or seg >= 60:
    print("Dados inválidos inseridos.")
else:
    print(f'O evento se iniciará as {hor}:{minu}:{seg}')
    if segenc >= 60:
        segenc = segenc - 60
        minuenc = minuenc + 1
    if minuenc >= 60:
        minuenc = minuenc - 60
        horenc = horenc + 1
    if horenc >= 24:
        horenc = horenc - 24
    print(f'O evento terá a duração de {durh} horas, {durm} minutos e {durs} segundos, sendo encerrado as '
          f'{horenc}:{minuenc}:{segenc}')
