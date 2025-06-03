# escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
import random
from time import sleep

computador = random.randint(0,5)

print('='*20)
print("JOGO DA ADIVINHAÇÃO")
print("="*20)

nome = input("antes de jogar, qual é o seu nome?: ")

print(f"olá {nome}! vou pensar em um número entre 0 e 5, tente adivinhar...")


print('='*20)
print("pensando...")
print("="*20)
sleep(2)
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
jogador = int(input(f"{nome}, qual número eu pensei?: "))


# o programa deverá escrever na tela se o usuário venceu ou perdeu
if jogador == computador:
    print('='*20)
    print(f"computador: {computador}")
    print(f"{nome}: {jogador}")
    print("você pensou o mesmo número que eu! parabéns!")
else:
    print('='*20)
    print(f"computador: {computador}")
    print(f"{nome}: {jogador}")
    print(f"que pena! você errou, tente na próxima!")
