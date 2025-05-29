def funcao_hash(chave, tamanho):
    # converte a chave em um número inteiro baseado na soma dos códigos de caractere
    if not isinstance(chave,str):
        raise TypeError("A chave deve ser uma String")
    return sum(ord(char) for char in chave) % tamanho

class TabelaHash:
    def __init__(self, tamanho):
        # Inicializa a tabela com uma lista (para tratamento de colisões)
        self.size = tamanho
        self.table = [[] for _ in range(tamanho)]

    def setar_item(self, chave, valor):
        # calcula o índice usando a função hash
        indice = funcao_hash(chave, self.size)
        # Verifica se a chave já existe no índice e atualiza
        for par in self.table[indice]:
            if par[0] == chave:
                par[1] = valor
                return
        # se a chave não existir adiciona um novo par chave-valor
        self.table[indice].append([chave,valor])

    def obter_item(self, chave):
        # calcula o índice usando a função hash
        indice = funcao_hash(chave, self.size)
        for par in self.table[indice]:
            if par[0] == chave:
                return par[1]
        # se a chave não for encontrada, retorne none
        return None
    
    def remover_item(self,chave):
        # calcula o índice usando a função hash
        indice = funcao_hash(chave,self.size)
        #encontra a chave e remove o par chave-valor
        for par in self.table[indice]:
            if par[0] == chave:
                self.table[indice].remove(par)
                return
            
    def __repr__(self):
        #representação da tabela hash para exibição
        return str(self.table)
    
#exemplo de uso
tabela_hash = TabelaHash(10) # Tabela com 10 posições
tabela_hash.setar_item("Bruno","333")
tabela_hash.setar_item("Theo","123")
tabela_hash.setar_item("Josi","222")
tabela_hash.setar_item("Bruce","444")
tabela_hash.setar_item("ziggie","567")
tabela_hash.setar_item("Michael","987")

print(tabela_hash) # exibe a tabela hash

#busca por um item
print(f"telefone {tabela_hash.obter_item("Bruno")}")
print(f"telefone {tabela_hash.obter_item("Bruce")}")

