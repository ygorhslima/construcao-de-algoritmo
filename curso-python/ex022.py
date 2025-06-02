nome = str(input("digite seu nome completo: ")).strip()

print(f"Frase em maiúsucula {nome.upper()}")
print(f"Frase em minúscula {nome.lower()}")
print(f"quantas letras ao todo?: {len(nome.replace(' ',''))}")
print(f"quantas letras tem o primeiro nome?: {len(nome.split()[0])}")