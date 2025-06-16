from random import randint
from time import sleep

lista = []
jogos = []
print("-="*40)
print("JOGA NA MEGA SENA".center(40))
print("-="*40)
sleep(0.7)
quant = int(input("quantos jogos você quer que eu sorteie: "))

tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print(f"-="*3, 'SORTEANDO {quant} jogos','-='*3)

for i, l in enumerate(jogos):
    print(f"jogo {i+1}: {l}")
    sleep(1)
print(f"os números sorteados foram {jogos}")
print("-="*30)