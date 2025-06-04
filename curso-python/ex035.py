#desenvolva um programa que leia o comprimento da três retas e diga ao usuário se elas podem ou não formar triângulos

print("-="*20)
print("analisador de triângulos")
print("-="*20)

r1 = float(input("digite a primeira reta: "))
r2 = float(input("digite a segunda reta: "))
r3 = float(input("digite a terceira reta: "))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print("os segmentos acima PODEM FORMAR triângulo")
else:
    print("os segmentos acima NÃO PODEM FORMAR triângulo")
