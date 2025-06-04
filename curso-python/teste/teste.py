nome = str(input("qual é seu nome: "))

if nome == "Ygor":
    print("que nome bonito")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("seu nome é bem popular no Brasil")
elif nome in 'Ana Claudia Jessica Juliana':
    print("belo nome feminino")
else:
    print("seu nome é bem normal")


print(f"tenha um bom dia, {nome}!")