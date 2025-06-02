from collections import deque

grafo = {}

grafo["vc"] = ["Joanilda","Carlendson","Danisvaldo"] # Amigos

grafo["Joanilda"] = ["Cleonistica","Marlindson"]
grafo["Carlendson"] = ["Adalgiza","Gabrandeia"]
grafo["Danisvaldo"] = ["Carlisto"]

grafo["Cleonistica"] = []
grafo["Marlindson"] = []
grafo["Adalgiza"] = []
grafo["Gabrandeia"] = []
grafo["Carlisto"] = []


def pesquisa_largura(letra_vendedor):
    fila_pesquisa = deque()
    fila_pesquisa += grafo["vc"]
    encontrado = False
    verificados = []
    while fila_pesquisa:
        pessoa=fila_pesquisa.popleft()
        
        if not pessoa in verificados:
            if(pessoa[0]==letra_vendedor):
                print(f"{pessoa} é um vendedor de ovos")
                encontrado=True
                return True
            else:
                verificados.append(pessoa)
                fila_pesquisa+=grafo[pessoa]
    if not encontrado:
        print("Vendedor não encontrado")

pesquisa_largura("M")

