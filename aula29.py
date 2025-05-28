def funcao_hash(chave, elemento):
    # converte a chave em um número inteiro baseado na soma dos códigos de caractere
    return sum(ord(char) for char in chave) % tamanho

class TabelaHash:
    def __init__(self, tamanho):
        # Inicializa a tabela com uma lista (para tratamento de colisões)
        