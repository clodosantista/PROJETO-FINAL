from datetime import datetime
from Pessoas import PessoaFisica, Endereco, PessoaJuridica

def main():
    lista_pf = []
    lista_pj = []

    while True:
        opcao = input("Escolha uma opção: 1 - Pessoa Física / 2 - Pessoa Jurídica / 3 - Remover Pessoa Física / 4 - Remover PJ / 0 - Sair: ")
        if not opcao.isdigit():
            print("Opção inválida! Por favor, digite um número.")
            continue
        opcao = int(opcao)

        if opcao == 1:
            while True:
                opcao_pf = input("Escolha uma opção: 1 - Cadastrar Pessoa Física / 2 - Listar Pessoa Física / 0 - Sair: ")
                if not opcao_pf.isdigit():
                    print("Opção inválida! Por favor, digite um número.")
                    continue
                opcao_pf = int(opcao_pf)

                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome de pessoa física: ")
                    novapf.cpf = input("Digite o CPF: ")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente números): "))

                    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (datetime.today().date() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos")
                        continue

                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)
                    print("Cadastro realizado com sucesso!")

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'Nome: {cada_pf.nome}')
                            print(f'CPF: {cada_pf.cpf}')
                            print(f'Endereço: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}')
                            print(f'Data Nascimento: {cada_pf.dataNascimento.strftime("%d/%m/%Y")}')
                            print(f'Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}')
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("Opção inválida! Por favor, digite uma das opções abaixo:")

        elif opcao == 2:
            while True:
                opcao_pj = input("Escolha uma opção: 1 - Cadastrar Pessoa Jurídica / 2 - Listar Pessoa Jurídica / 0 - Sair: ")
                if not opcao_pj.isdigit():
                    print("Opção inválida! Por favor, digite um número.")
                    continue
                opcao_pj = int(opcao_pj)

                if opcao_pj == 1:
                    novapj = PessoaJuridica()
                    novo_end_pj = Endereco()

                    novapj.nome = input("Digite o nome da empresa: ")
                    novapj.cnpj = input("Digite o CNPJ: ")
                    novapj.rendimento = float(input("Digite o rendimento mensal (Digite somente números): "))

                    novo_end_pj.logradouro = input("Digite o logradouro: ")
                    novo_end_pj.numero = input("Digite o número: ")
                    end_comercial = input("Este endereço é comercial? S/N: ")
                    novo_end_pj.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapj.endereco = novo_end_pj

                    lista_pj.append(novapj)
                    print("Cadastro realizado com sucesso!")

                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f'Nome: {cada_pj.nome}')
                            print(f'CNPJ: {cada_pj.cnpj}')
                            print(f'Endereço: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}')
                            print(f'Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento)}')
                            print("Digite 0 para sair")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao_pj == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("Opção inválida! Por favor, digite uma das opções abaixo:")

        elif opcao == 3:
            cpf_remover = input("Digite o CPF da Pessoa Física a ser removida: ")
            lista_pf = [pf for pf in lista_pf if pf.cpf != cpf_remover]
            print("Pessoa Física removida com sucesso!")

        elif opcao == 4:
            cnpj_remover = input("Digite o CNPJ da Pessoa Jurídica a ser removida: ")
            lista_pj = [pj for pj in lista_pj if pj.cnpj != cnpj_remover]
            print("Pessoa Jurídica removida com sucesso!")

        elif opcao == 0:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida! Por favor, digite uma das opções abaixo:")

if __name__ == "__main__":
    main()

