# Pergunta o valor da casa
valor_casa = float(input("Qual o valor da casa?: R$").replace("R$", "").replace(".", "").replace(",", ".").strip())

# Pergunta o salário do comprador
salario_comprador = float(input("Qual o seu salário?: R$").replace("R$", "").replace(".", "").replace(",", ".").strip())

# Pergunta em quantos anos será pago
anos_pagamento = int(input("Quantos anos você vai pagar a casa?: "))

# Calcula o valor da prestação
prestacao_mensal = valor_casa / (anos_pagamento * 12)

# Calcula 30% do salário
limite_prestacao = salario_comprador * 0.3

# Verifica se a prestação está dentro do limite
if prestacao_mensal <= limite_prestacao:
    print(f"✅ Empréstimo aprovado! Prestação mensal: R$ {prestacao_mensal:.2f}")
else:
    print(f"❌ Empréstimo negado! Prestação de R$ {prestacao_mensal:.2f} excede 30% do salário (R$ {limite_prestacao:.2f})")
