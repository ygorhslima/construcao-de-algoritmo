#quantidade de km percorrido
km = float(input("quantos km percorrido: ")) # 100km
dias = int(input("quantos dias o carro foi alugado: ")) # 4 dias
#calculo do preco
# carro custa R$60 por dia
# R$0.15 por km rodado
pago = (dias * 60) + (km * 0.15)
print(f"o total a pagar é de {pago:.2f}")

