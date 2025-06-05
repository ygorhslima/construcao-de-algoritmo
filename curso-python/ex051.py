a1 = int(input("Primeiro termo: "))
r = int(input("razão: "))

print("os 10 primeiros termos da PA são: ")
for i in range(10):
    termo = a1 + i * r
    print(termo, end="->")