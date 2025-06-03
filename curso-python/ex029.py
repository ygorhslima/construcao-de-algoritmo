# escreva um programa que leia a velocidade de um carro
vel = float(input("velocidade do carro(km):"))
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# a multa vai custar R$7,00 por cada km acima do limite
if vel > 80:
    excesso = vel - 80
    multa = 7 * excesso
    print("você foi multado")
    print(f"a sua multa vai custa R${multa}")
else:
    print("Você está na velocidade correta. Continue assim!")