# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.

valor1 = int(input("digite o valor1"))

valor_final = valor1 + 12/100 * valor1

print(f"o valor do produto é = {valor_final}")