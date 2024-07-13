import textwrap

#criação de usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))




#funções de validação
def excedeuSaldo(valor, saldo):
    return  valor > saldo

def excedeuLimite(valor,limite):
    return valor > limite

def excedeuSaques(numero_saques, limite_saques):
    return numero_saques >= limite_saques


# função para depósito 
def deposito( valor,saldo, extrato, /):
    if valor >= 0:
       saldo += valor
       extrato += f"Depósito: R$ {valor:.2f}\n"
       print(f"Depósito de : R$ {valor} realizado com sucesso! Seu saldo atual é de: R$ {saldo:.2f}.")
    else:
       print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# função para saque 
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if excedeuSaques(numero_saques,limite_saques):       
        print("Operação falhou! Número máximo de saques excedido. O limite de saques diários é de 3. Para aumentar o limite por favor entre em contato com o seu gerente.")
    elif excedeuSaldo (valor,saldo):
        print(f"Operação falhou! Você não tem saldo suficiente. Seu saldo atual é de: R$ {saldo:.2f}.")
    elif excedeuLimite (valor,limite):
        print("Operação falhou! O valor do saque excede o limite.O limite da sua conta é de R$ 500.00. Para aumentar o limite por favor entre em contato com o seu gerente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"saque realizado com sucesso! Seu saldo atual é de: R$ {saldo:.2f}.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

# função para extrato
def mostrarExtrato (saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    return extrato

#função de operações bancárias 
def menu():
    menu = """\n
    Bem vindo ao Banco Dio Python! Selecione a opção do menu para continuar:

    ================ MENU ================
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [C]\tNova conta
    [L]\tListar contas
    [U]\tNovo usuário
    [Q]\tSair
    => """
    return input(textwrap.dedent(menu))

def inicio():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuario = []
    contas = []
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    while True:
        opcao = menu()
        if opcao == 'D':
            saldo, extrato = deposito(float(input("Informe o valor do depósito: ")),saldo, extrato)
        elif opcao == 'S':
             valor = float(input("Informe o valor do saque: "))
             saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
             )
        elif opcao == 'E':
             mostrarExtrato (saldo, extrato=extrato)
        elif opcao == 'Q':
            print ("obrigada por usar os serviços do banco Dio! Volte Sempre")
            break
        else:
            print ("Menu " + opcao)
            print ("ocorreu um erro, operação cancelada, tente novamente mais tarde")
            break
 

inicio()