#escreva um progrma que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
a = int(input("1° número: "))
b = int(input("2° número: "))

#- O primeiro valor é maior
if a > b:
    print(f"{a} é maior do que {b}")
#- O segundo valor é maior
elif b > a:
    print(f"{b} é maior do que {a}") 
#- Não existe valor maior, os dois são iguais 
elif a == b:
    print(f"{a} é igual a {b}")

