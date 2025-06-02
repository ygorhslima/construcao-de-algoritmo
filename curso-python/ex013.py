salario = float(input("qual é o salário do funcionário: R$"))
novo = salario + (salario * 15/100)
print("um funcionáro que ganhava R${:.2f} com 15% de aumento, passa a receber R${:.2f}".format(salario,novo))