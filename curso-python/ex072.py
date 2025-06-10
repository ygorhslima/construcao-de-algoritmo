# * Crie um programa
# * que tenha uma tupla totalmente 
# * preenchida com uma contagem por extenso, de zero até vinte
# * 
# * seu programa deverá ler um número pelo teclado (entre 0 e 20) 
# * e mostrá-lo por extenso
# *

contagem = (
    "Zero","Um","Dois","Três","Quatro","Cinco","Seis","Sete","Oito",
    "Nove","Dez","Onze","Doze","Treze","Catorze","Quinze","Dezesseis","Dezessete",
    "Dezoito","Dezenove","Vinte"
)

while True:
    n = int(input("digite um número entre 0 e 20: "))

    if n >= 0 and n <= 20:
        print(f"você digitou o número {contagem[n]}")
        break
    else:
        n = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    
