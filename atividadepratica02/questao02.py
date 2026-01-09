produto = input("Digite o nome do produto: ")
valor_produto = float(input("Digite o valor do produto: "))
desconto = 20

valor_desconto = valor_produto * (desconto / 100)
valor_final = valor_produto - valor_desconto

print(f"Produto: {produto}")
print(f"Preço Unitário: R$ {valor_produto:.2f}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço total: R$ {valor_final:.2f}")