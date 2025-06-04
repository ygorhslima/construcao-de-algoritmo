from datetime import datetime
#faça um programa que 

# leia o ano de nascimento de um jovem e informe de acordo com sua idade
ano_nascimento = int(input("qual o seu ano de nascimento?: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento


# se já é a hora de se alistar
if idade == 18:
    print(f"você tem {idade} anos e está na idade certa para se alistar, vá a uma junta militar mais próxima!")
# Se ele ainda vai se alistar ao serviço militar
elif idade < 18:
    print(f"você tem {idade} anos e ainda não pode se alistar")
# se já passou do tempo de alistamento
else:
    print(f"você tem {idade} anos e já passou o seu processo de alistamento")


# seu programa também deverá mostrar o tempo que falta ou que passou do prazo
