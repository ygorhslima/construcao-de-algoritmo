# crie um programação que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'

cidade = str(input("digite um nome de uma cidade: ")).strip().lower()
# verificando o nome da cidade, o split vai dividir a frase e vai pegar no índice 0 a primeira palavra, se for santo retorna True, senão, retorna False
verificar_nome = cidade.split()[0] == "santo"
print(f"A cidade começa com santo?: {verificar_nome}")