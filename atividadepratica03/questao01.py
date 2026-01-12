idade = int(input("Digite a idade: "))

if idade <0:
    print("idade inválida")
elif idade <= 12:
    print("criança")
elif idade <= 17:
    print("adolecente")
elif idade <= 59:
    print("adulto")
else:
    print("idoso")