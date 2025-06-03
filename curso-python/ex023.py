# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

#ex: digite um número: 1834
#unidade: 4
#dezena:3
#centena:8
#milhar:1

n = int(input("digite um número entre 0 e 9999: "))

unidade = n % 10 
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10

print(f"unidade: {unidade}")
print(f"dezena: {dezena}")
print(f"centena: {centena}")
print(f"milhar: {milhar}")
