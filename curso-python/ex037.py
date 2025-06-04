import math
#escreva um programa que

#  leia um número qualquer
n = int(input("leia um número qualquer: "))

#  peça para o usuário escolher qual será a base de conversão
print(f"\033[4;31m {'-='*10} MENU {'-='*10} \033[m")
print("escolha sua operação: ")
print("\033[33m[ 1 ] para binário \033[m")
print("\033[34m[ 2 ] para octal \033[m")
print("\033[35m[ 3 ] para hexadecimal \033[m")

operacao = int(input("escolha uma das operações acima: "))
if operacao == 1:
    binario = bin(n)
    print(f"{n} em binário: {binario}")
elif operacao == 2:
    octal = oct(n)
    print(f"{n} em octal: {octal}")
else:
    hexadecimal = hex(n)
    print(f"{n} em hexadecimal: {hexadecimal}")