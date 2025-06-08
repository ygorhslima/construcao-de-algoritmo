# faça um programa que leia um número qualquer e mostre seu fatorial

# ex:
# 5! = 5x4x3x2x1 = 120

n = int(input("digite um número para calcular seu fatorial:"))
contador = n
fat = 1

print(f"{n}! = ", end="")

while contador > 0:
    print(f"{contador}", end="")
    print(" x " if contador > 1 else " = ", end="")
    fat *= contador
    contador -= 1

print(fat)