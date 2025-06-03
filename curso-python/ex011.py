#leia a largura e altura de uma parede
largura = float(input("Largura(m): "))
altura = float(input("altura(m): "))
#calcule a area
area = largura * altura
#quantidade de tinta necessário para pinta-lo
tinta = area / 2
print(f"a parede tem tamanho {largura}x{altura}m e sua área é {area}m², é preciso de {tinta}L de tinta para pinta-la")