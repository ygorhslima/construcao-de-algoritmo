#leia duas notas
nome = str(input("digite o nome do aluno: "))
n1 = float(input(f"digite a 1° nota do aluno {nome}: "))
n2 = float(input(f"digite a 2° nota do aluno {nome}: "))
# calcule a média
media = (n1 + n2) / 2
# mostre a média
print("{:=^20}".format(nome))
print(f"nota1: {n1}")
print(f"nota2: {n2}")
print(f"média: {media}")
