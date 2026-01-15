def calcular_gorjeta (valor_conta, porcentagem_gorjeta):
    gorgeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorgeta

valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(valor, porcentagem)

print(f"O valor da gorjeta é {gorjeta:.2f}")