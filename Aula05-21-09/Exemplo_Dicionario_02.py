# Construa um dicionário com nome, salariobruto, salario liquido, 
# para número indeterminado de pessoas, nele será calculado o 
# desconto de 8% do INSS e de 10% para IRPF. Preciso que o 
# programa seja escrito na Linguagem Python de forma Otimizada..


def main():
    # Cria um dicionário vazio
    folha_de_pagamento = {}

    # Lê os dados da folha de pagamento
    while True:
        # Lê o nome e o salário bruto
        nome = input("Digite o nome: ")
        salario_bruto = float(input("Digite o salário bruto: "))

        # Calcula o desconto do INSS
        desconto_inss = salario_bruto * 0.08

        # Calcula o desconto do IRPF
        desconto_irpf = 0
        if salario_bruto > 1903.98:
            desconto_irpf = salario_bruto * 0.10

        # Calcula o salário líquido
        salario_liquido = salario_bruto - desconto_inss - desconto_irpf

        # Adiciona os dados ao dicionário
        folha_de_pagamento[nome] = {
            "salario_bruto": salario_bruto,
            "desconto_inss": desconto_inss,
            "desconto_irpf": desconto_irpf,
            "salario_liquido": salario_liquido,
        }

        # Pergunta se o usuário deseja continuar
        continuar = input("Deseja continuar? (s/n): ")
        if continuar != "s":
            break

    # Imprime os itens do dicionário
    for nome, dados in folha_de_pagamento.items():
        print(nome, dados["salario_bruto"], dados["desconto_inss"], dados["desconto_irpf"], dados["salario_liquido"])


if __name__ == "__main__":
    main()
