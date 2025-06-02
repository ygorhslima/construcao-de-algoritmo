from random import randint

sorteio = randint(1,4)

a1 = str(input("Aluno 1: ")) 
a2 = str(input("Aluno 2: "))
a3 = str(input("Aluno 3: "))
a4 = str(input("Aluno 4: "))

alunos = [a1,a2,a3,a4]

print(f"o aluno escolhido foi: {alunos[sorteio-1]} ")