prem = float(input("Informe o valor do prêmio: R$ "))
gan1 = int(input("Informe a porcentagem(%) investida pelo primeiro ganhador: "))
gan2 = int(input("Informe a porcentagem(%) investida pelo segundo ganhador: "))
gan3 = int(input("Informe a porcentagem(%) investida pelo terceiro ganhador: "))
if gan1 + gan2 + gan3 > 100:
    print("Operação Inválida, os ganhadores não podem receber mais de 100% do prêmio,"
          " certifique - se dos valores inseridos.")
elif gan1 + gan2 + gan3 < 100:
    print("O prêmio não pode ter sobras, certifique - se dos valores inseridos.")
else:
    print(f'O primeiro ganhador receberá: R$ {prem * gan1 * 100}\n'
          f'O segundo ganhador receberá: R$ {prem * gan2 * 100}\n'
          f'O terceiro ganhador receberá: R$ {prem * gan3 * 100}\n')
