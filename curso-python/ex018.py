import math

#leia um angulo qualquer
angulo = float(input("Valor do ângulo em graus: "))

angulo_radianos = math.radians(angulo)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")