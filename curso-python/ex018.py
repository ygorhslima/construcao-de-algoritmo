from math import radians,sin,cos,tan

#leia um angulo qualquer
angulo = float(input("Valor do ângulo em graus: "))

angulo_radianos = radians(angulo)

seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")