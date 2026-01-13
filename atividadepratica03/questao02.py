peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

imc = peso / (altura ** 2)

print("Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")