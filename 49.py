hor = int(input("Informe a atual hora: "))
min = int(input("Informe o atual minuto: "))
seg = int(input("Informe o atual segundo: "))
durh = int(input("Informe as horas de duração do evento: "))
durm = int(input("Informe os minutos de duração do evento(Acompanha as horas inseridas anteriormente): "))
durs = int(input("Informe os segundos de duração do evento(Acompanha as horas e minutos inseridos anteriormente): "))
if hor + durh >= 24 and min + durm >= 60 and seg + durs >= 60:
    print(f'O horário de termino da reunião é as {((hor + durh) - 24) + 1}:{((min + durm) - 60) + 1}:'
          f'{(seg + durs) - 60}')
elif hor + durh >= 24 and min + durm >= 60:
    print(f'O horário de termino da reunião é as {((hor + durh) - 24) + 1}:{(min + durm) - 60}:{seg + durs}')
elif min + durm >= 60 and seg + durs >= 60:
    print(f'O horário de termino da reunião é as {hor + durh+ 1}:{((min + durm) - 60) + 1}:{(seg + durs) - 60}')
elif hor + durh >= 24:
    print(f'O horário de termino da reunião é as {(hor + durh) - 24}:{min + durm}:{seg + durs}')
elif min + durm >= 60:
    print(f'O horário de termino da reunião é as {hor + durh + 1}:{(min + durm) - 60}:{seg + durs}')
elif seg + durs >= 60:
    print(f'O horário de termino da reunião é as {hor + durh}:{min + durm + 1}:{(seg + durs) - 60}')
