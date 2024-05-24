import time
import textwrap

print("\n       ᗷᗩᑎᛕ Ꭵᗯᗩ\n")
print("\nAqui o seu dinheiro rende mais\n")

def menu():  
    menu = '''

    [0] Depósito     

    [1] Saque 

    [2] Extrato

    [3] Abrir conta 

    [4] Listar Contas 

    [5] Novo Usuário      

    [S] Fechar/Sair

    =>  '''

    return input(textwrap.dedent(menu))

# Função para depósito (0)
def deposit_value(saldo, valor, extrato, /): # Deve ser chamado por posição ARGS
    if valor > 0:  # O valor do depósito sempre deve ser positivo
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"

        # Coloca o programa para dormir pelo tempo determinado
        time.sleep(1) 
        print("\nDepósito feito com sucesso!\n")

    else:
          print("\033[1;31mOperação falhou! Formato inválido.\033[m]")
        
    return saldo, extrato

#Função para Saque (1)
def withdrawal_value(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # * para forma nomeada 
    excedeu_saldo = valor > saldo #Se o valor de saque desejado for maior que saldo.
    excedeu_limite = valor > limite #Se o valor excedeu o valor limmite de saque. 
    excedeu_saques = numero_saques >= limite_saques  #Se a quantidade de saques ultrapassou o limite diário.
    sucesso_saque = valor <= limite

    if excedeu_saldo:
         time.sleep(1)
         print("\033[0;31mFalha na operação! Saldo insuficiente!\033[m") # Houve mudança na cor das letras no terminal.

    elif excedeu_limite:
         time.sleep(1)
         print("\033[0;31mFalha na operação! O valor do saque é maior que o limite permitido.\033[m")

    elif excedeu_saques:
         time.sleep(1)
         print("\033[0;31mFalha na operação! Você alcançou o limite de saques.\033[m")

    elif sucesso_saque:
        valor > 0
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1  #Para tentativa de saque negativa
        
        time.sleep(2)
        print("Saque realizado com sucesso!\n")
           
    else: 
        print("\033[31mFalha na operação! O valor informado é invalido.\033[m")

    return saldo, extrato 

#Função para Extrato (2)
def bank_statement_value(saldo, /, *, extrato): 
    time.sleep(2)

    print("========== \033[1m Extrato \033[m ==========")
    print("Não foram realizadas movimentações" if not extrato else extrato)  
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("================================")
 
# Função para criação de usuário (5)
def creat_users(users):  
    cpf = input("Informe somente os números do seu CPF:\n ")
    user = filter_users(cpf, users)

    if user: 
        print("\nEste CPF já está cadastrado!\n")
        return
    
    nome = input("\nInforme seu nome completo: \n")
    data_nascimento = input("\nInforme a data do seu nascimento no formato dd-mm-aaaa: \n")
    endereco = input("\nInforme seu endereço (logradouro, N° - bairro- cidade/sigla estado):\n ")

    users.append({"nomme": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("\nUsuário criado com sucesso!\n")

# Filtrar os usuários
def filter_users(cpf, users):
    usuarios_filtrados = [user for user in users if user["cpf"] == cpf ] # Verifica se o cpf passado já existe
    return usuarios_filtrados[0] if usuarios_filtrados else None   # verificando se usuariois_filtrados é uma lista vazia, caso não, retorna o primeiro elemento, caso não encontre retorne None

# Nova conta (3)
def open_account(agencia, number_account, users): 
    cpf = input("Informe seu CPF: ")
    user = filter_users(cpf, users)

    if user: 
        print("\nConta criada com sucesso!\n Bem Vindo ao Banco IWA!")
        return {"agencia": agencia, "number_account": number_account, "users": users}
    
    print("\n Usuário não identificado, criação de conta encerrada! 😭")

# Função para listagem de contas (4)
def listar_contas(contas): 
    for conta in contas: 
        linha = f"""\
            Agência: \t{conta["agencia"]}
            C/C:\t\t{conta["number_account"]}
            Titular:\t{conta["user"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha)) 




def main():
    LIMITES_SAQUES = 3
    AGENCIA = "0001"

    contas = []
    users = []
    saldo = 0 
    limite = 500 
    extrato = " "
    numero_saques = 0
    


    while True:
        
        opcao = menu()

        if opcao == "0":
            valor = float(input("Informe qual o valor que deseja depositar: "))

            saldo, extrato = deposit_value(saldo, valor, extrato) # funções podem alterar variaveis, mais tem escopos própios. 
            time.sleep(2)

        elif opcao == "1":
            valor = float(input("Informe o valor que deseja sacar: "))

            saldo, extrato = withdrawal_value(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITES_SAQUES,
            )

            time.sleep(2)

        elif opcao == "2":
            bank_statement_value(saldo, extrato=extrato)
            time.sleep(2)

        elif opcao == "3":    
            number_account = len(contas) + 1 
            conta = open_account(AGENCIA, number_account, users)

            if conta: 
                contas.append(conta)

            time.sleep(2)

        elif opcao == "4":
            listar_contas(contas)
            time.sleep(2)

        elif opcao == "5":  
            creat_users(users)
            time.sleep(2)

        elif opcao == "S":
            print("Fim da operação!")
            break

        else:
            print("\nOpção não identificada! Por favor selecione novamente a operação desejada.\n")


main()