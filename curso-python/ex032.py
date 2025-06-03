# faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input("digite um ano qualquer: "))

#Um ano é bissexto se:
#1. É divisível por 4
#e
#Não é divisível por 100
#OU
#É divisível por 400
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")