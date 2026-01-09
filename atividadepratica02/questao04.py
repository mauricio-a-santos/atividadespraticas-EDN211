km_percorrido = float(input("Digite a distância percorrida em km: "))
combustivel_gasto = float(input("Digite o combustível gasto em litros: "))

consumo_medio = km_percorrido / combustivel_gasto

print(f"Consumo médio: {consumo_medio:.2f} mk/l")
print(f"Distância percorrida: {km_percorrido:.2f}")
print(f"Combustível gasto: {combustivel_gasto:.2f} L")