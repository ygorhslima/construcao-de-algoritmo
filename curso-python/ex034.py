# escreva um programa que:

#  pergunte o salário de um funcionário
salario = float(input("digite o salário do funcionário: "))

#  calcule o valor do seu aumento:

#para salários superiores a R$1.250,00, calcule um aumento de 10%
if salario > 1250.00:
    aumento = salario * (10/100)
    novo_salario = salario + aumento
    print(f"o salário do funcionário é de {salario} e com aumento de 10% ficou {novo_salario}")


# para os inferiores ou iguais, o aumento é de 15%
if salario <= 1250:
    aumento = salario * (15/100)
    novo_salario = salario + aumento
    print(f"o salário funcionário é de {salario} e com aumento de 15% ficou {novo_salario}")