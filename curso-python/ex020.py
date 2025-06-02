import random 

a1 = str(input("Aluno 1: ")) 
a2 = str(input("Aluno 2: "))
a3 = str(input("Aluno 3: "))
a4 = str(input("Aluno 4: "))

alunos = [a1,a2,a3,a4]
random.shuffle(alunos)

print(f"{'='*20}ORDEM DE APRESENTAÇÃO{'='*20}")
print(f"1° - {alunos[0]}")
print(f"2° - {alunos[1]}")
print(f"3° - {alunos[2]}")
print(f"4° - {alunos[3]}")
