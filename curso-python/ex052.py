num = int(input("digite um número: "))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print("{}".format(c),end=' ')

print(f"\n\033[mo número {num} foi dividido {tot} vezes")
if tot == 2:
    print("por isso que é primo")
else:
    print("por isso que não é primo")