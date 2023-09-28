# Crie um dicionário que é uma agenda e coloque nele os seguintes dados: chave (cpf), 
# nome, idade, telefone. O programa deve ler um número indeterminado de dados, criar a 
# agenda e imprimir todos os itens do dicionário no formato chave: nome, idade, fone.

def main():
    # Cria um dicionário vazio
    agenda = {}

    # Lê os dados da agenda
    while True:
        cpf = input("Digite o CPF: ")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        telefone = input("Digite o telefone: ")

        # Adiciona os dados ao dicionário
        agenda[cpf] = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone,
        }

        # Pergunta se o usuário deseja continuar
        continuar = input("Deseja continuar? (s/n): ")
        if continuar != "s":
            break

    # Imprime os itens do dicionário
    for cpf, contato in agenda.items():
        print(cpf, contato["nome"], contato["idade"], contato["telefone"])


if __name__ == "__main__":
    main()
