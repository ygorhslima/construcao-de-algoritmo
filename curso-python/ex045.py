from time import sleep
from random import randint

sleep(0.5)
print("-="*30)
print("\033[0;31mGAME: PEDRA, PAPEL E TESOURA!\033[m")
print("-="*30)
sleep(0.5)

print("\033[0;33;44msuas opções: \033[m")
print("\033[31m[ 0 ]Pedra\033[m")
print("\033[33m[ 1 ]Papel\033[m")
print("\033[34m[ 2 ]Tesoura\033[m")

jogador = int(input("Qual é sua jogada?: ")) # jogador faz sua jogada
computador = randint(0,2) # computador faz sua jogada

print("JO")
sleep(0.3)
print("KEN")
sleep(0.3)
print("PO!")

# CASO 1: PEDRA E PAPEL
if (jogador == 0 and computador == 1):
    print("jogador jogou Pedra")
    print("computador jogou Papel")
    print("computador venceu")
elif (jogador == 1 and computador == 0):
    print("jogador jogou Papel")
    print("computador jogou Pedra")
    print("jogador venceu")

# CASO 2: PEDRA E TESOURA
elif (jogador == 2 and computador == 0):
    print("jogador jogou tesoura")
    print("computador jogou pedra")
    print("computador venceu")
elif(jogador == 0 and computador == 2):
    print("jogador jogou pedra")
    print("computador jogou tesoura")
    print("jogador venceu")

# CASO 3: TESOURA E PAPEL
elif (jogador == 1 and computador == 2):
    print("jogador jogou papel")
    print("computador jogou tesoura")
    print("computador venceu")
elif (jogador == 2 and computador == 1):
    print("jogador jogou tesoura")
    print("computador jogou papel")
    print("jogador venceu")


elif (jogador == 0 and computador == 0) or (jogador == 1 and computador == 1) or (jogador == 2 and computador == 2):
    print("deu empate")