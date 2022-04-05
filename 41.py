prec = float(input("Informe e valor da hora de trabalho: "))
horas = int(input("Informe a quantidade de horas trabalhadas durante o mês: "))

print(f'O valor a ser recebido é de R$ {prec * horas + (prec * horas * 0.1)}')
