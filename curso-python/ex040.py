# crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
# de acordo com a média atingida
# - média abaixo de 5.0:
    # - reprovado
# - média entre 5.0 e 6.9
    # - Recuperação
# - média 7.0 ou superior
    # - Aprovado

n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
media = (n1+n2) / 2
print(f"você tirou as notas {n1} e {n2} e sua média foi {media:.2f}")

if media < 5.0:
    print("reprovado")
elif media >= 5.0 and media < 7.0:
    print("Recuperação")
else:
    print("aprovado")


