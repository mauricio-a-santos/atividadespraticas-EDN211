valor_real = float(input("Digite o valor em reais: "))
taxa_dolar = 5.37
taxa_euro = 6.25

valor_dolar = valor_real / taxa_dolar
valor_euro = valor_real / taxa_euro

print(f"Valor em reais: R$ {valor_real:.2f}")
print(f"Valor em Dolar: R$ {valor_dolar:.2f}")
print(f"Valor em Euro: R$ {valor_euro:.2f}")