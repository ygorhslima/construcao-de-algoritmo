import math 
cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)
print(f"o calculo da hipotesuna foi de {hipotenusa}")