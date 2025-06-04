from datetime import datetime
# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta

# leia o ano de nascimento de um jovem e informe de acordo com sua idade
ano_nascimento = int(input("qual o seu ano de nascimento?: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento


# e mostre sua categoria, de acordo com a idade

# até 9 anos: Mirim
if idade <= 9:
    print("atleta mirim")
# até 14 anos: infantil
elif idade <= 14:
    print("atleta infantil")
# até 19 anos: Junior
elif idade <= 19:
    print("atleta Junior")
# até 20 anos: senior
elif idade <= 20:
    print("atleta Senior")
# acima: master
else:
    print("atleta master")

