prod = float(input("Informe o valor do produto: R$ "))
print(f'Valor do produto com desconto de 10% - R$ {prod - prod * 0.1}\n'
      f'Valor das parcelas do produto dividido em 3X - R$ {prod / 3}\n'
      f'Valor da comissão do vendedor caso o produto seja vendido com desconto - R$ {(prod - prod * 0.1) * 0.05}\n'
      f'Valor da comissão do vendedor caso o produto seja vendido parcelado - R$ {prod * 0.05}')
