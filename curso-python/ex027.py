#faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente 

#ex: Ana Maria de Souza
#primeiro = ana
#ultimo = souza

nome = input("digite seu nome completo: ").strip()
print(f"primeiro = {nome.split()[0]}")
print(f"último = {nome.split()[-1]}")