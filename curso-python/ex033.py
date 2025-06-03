#faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input("1°número: "))
n2 = int(input("2°número: "))
n3 = int(input("3°número: "))

maior = n1
menor = n1

if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2

if n3 < menor:
    menor = n3

print(f"o número maior é {maior}")
print(f"e o número menor é {menor}")