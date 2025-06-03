#Faça um programa que leia uma frase pelo teclado e mostre
# quantas vezes aparece a letra A
# em que posição ela aparece a primeira vez
# em que posição ela aparece a última vez
frase = input("digite uma frase qualquer: ")
print(f"quantas vezes aparece a letra A?: {frase.count('a')}")
print(f"em que posição o primeiro A apareceu?: {frase.find('a')} ")
print(f"em que posição o A aparece a última vez?: {frase.rfind("a")}")