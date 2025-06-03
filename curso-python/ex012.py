#leia o preço de um produto
preco = float(input("qual o preço do produto?: "))
desconto = preco * (5/100)
novo_preco = preco - desconto
print(f"o preço anterior é de R${preco} e o seu novo preço com 5% de desconto é de R${novo_preco}")