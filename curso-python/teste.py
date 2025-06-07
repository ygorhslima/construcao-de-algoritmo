n = 1
somapar = 0
somaimpar = 0
tot = 0
while (n != 0):
    n = int(input("digite um valor: "))
    if (n != 0):
        if(n % 2 == 0):
            somapar += 1
        else:
            somaimpar += 1
    tot += 1

print("você digitou {} números pares e {} números ímpares".format(somapar,somaimpar))