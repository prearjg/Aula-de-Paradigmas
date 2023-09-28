def calcular_desconto_inss(salario_bruto):
    return salario_bruto * 0.08

def calcular_desconto_irpf(salario_bruto):
    return salario_bruto * 0.10 if salario_bruto > 1903.98 else 0

def main():
    agenda = {}
    folha_de_pagamento = {}

    while True:
        print("Escolha uma opção:")
        print("1. Adicionar contato")
        print("2. Calcular salário")
        print("3. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            cpf = input("Digite o CPF: ")
            nome = input("Digite o nome: ")
            idade = input("Digite a idade: ")
            telefone = input("Digite o telefone: ")
            
            agenda[cpf] = {
                "nome": nome,
                "idade": idade,
                "telefone": telefone,
            }
        elif opcao == "2":
            nome = input("Digite o nome do funcionário: ")
            salario_bruto = float(input("Digite o salário bruto: "))
            
            desconto_inss = calcular_desconto_inss(salario_bruto)
            desconto_irpf = calcular_desconto_irpf(salario_bruto)
            salario_liquido = salario_bruto - desconto_inss - desconto_irpf
            
            folha_de_pagamento[nome] = {
                "salario_bruto": salario_bruto,
                "desconto_inss": desconto_inss,
                "desconto_irpf": desconto_irpf,
                "salario_liquido": salario_liquido,
            }
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

    print("\nAgenda de Contatos:")
    for cpf, contato in agenda.items():
        print(f"CPF: {cpf}, Nome: {contato['nome']}, Idade: {contato['idade']}, Telefone: {contato['telefone']}")

    print("\nFolha de Pagamento:")
    for nome, dados in folha_de_pagamento.items():
        print(f"Nome: {nome}, Salário Bruto: {dados['salario_bruto']}, Desconto INSS: {dados['desconto_inss']}, Desconto IRPF: {dados['desconto_irpf']}, Salário Líquido: {dados['salario_liquido']}")

if __name__ == "__main__":
    main()
