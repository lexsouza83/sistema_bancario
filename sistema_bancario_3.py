#Modelando o codigo do sistema com POO
print('{:=^40}'.format(" BANCO DIO "))


#Definindo classes

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def operacao(self, conta, operacao):
        operacao.gravar(conta)

    def salvar_conta(self, conta):
        self.contas.append(conta)

class Pessoa_fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self. _agencia = "0001"
        self._cliente = cliente
        self._historico = Histórico()
    
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self.saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
           print("\nFalha! Saldo Inssuficiente")
           return True
        
        elif valor > 0:
            self._saldo -=valor
            print("\nSaque concluído!")
            return True
        
        else:
            print("\nOperação falhou! O valor inválido.")

class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saque = limite_saque

        def saque(self, valor):
            numero_saques = len ([operacao for operacao in self.historico.operacao if operacao["tipo"]== saque.__name__])
            excedeu_limite = valor > self._limite
            excedeu_saques = numero_saques >= self._limite_saques
            
            if excedeu_limite:
                print("Operação Falhou! Valor informado excede o limite")

            elif excedeu_saques:
                print("Operação Falhou! Limite de saques atingido!")

            else:
                return super().sacar(valor)
            
            return False
        

class Historico:
    def __init__(self):
        self.operacoes = []
        
        @property
        def operacoes(self):
            return self._operacoes
        
        def adicionar_operacao(self, operacao):
            self._operacoes.append({"tipo":operacao._class_._name_,
                                    "valor": operacao.valor,
                                    "data": datetime.now().strtime("%d-%m-$Y %H:%M:%s"),})
            
class Operacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_ooperacao = conta.sacar(self.valor)

        if sucesso_operacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Operacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_operacao = conta.depositar(self.valor)

        if sucesso_operacao:
            conta.historico.adicionar_operacao(self)

def painel():
    painel = """\n
    ================ SELECIONE A OPERAÇÃO DESEJADA ================
    [1] Deposito
    [2] Saque
    [3] Ver Extrato
    [4] Criar conta
    [5] Listar contas
    [6] Criar usuário
    [7] Sair
    => """
    return input(painel)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito concluido")
    else:
        print("\nOperação falhou! O valor inválido.")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nFalha! Saldo Inssuficiente")

    elif excedeu_limite:
        print("\nFalha! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nFalha! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque concluído! ")

    else:
        print("\n Operação falhou! Valor inválido.")

    return saldo, extrato

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (Números apenas): ")
    usuario = listar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (rua, nro - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print(" Usuário criado com sucesso!")

def listar_usuario(cpf, usuarios):
    usuarios_listados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_listados[0] if usuarios_listados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = listar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, criação de conta cancelada!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = painel()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "3":
            mostrar_extrato(saldo, extrato = extrato)


        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "7":
            print("Agradecemos a preferencia. Sistema Encerrado!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()