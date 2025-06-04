#refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:

r1 = float(input("digite a primeira reta: "))
r2 = float(input("digite a segunda reta: "))
r3 = float(input("digite a terceira reta: "))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print("os segmentos acima PODEM FORMAR triângulo")
    if r1 == r2 and r2 == r3 and r3 == r1:
        print("\033[31mEQUILÁTERO\033[m")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("\033[33mESCALENO\033[m")
    else:
        print("\033[34mISÓSCELES\033[m")
else:
    print("os segmentos acima NÃO PODEM FORMAR triângulo")



# - equilátero: todos os lados iguais
# - isósceles: dois lados iguais
# a - 4     a - 4
# b - 4     b - 5
# c - 5     c - 4
# - Escaleno: todos os lados diferente