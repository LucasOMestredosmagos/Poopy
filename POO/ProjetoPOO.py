class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.quartos = []
        self.reservas = []

    def adicionar_funcionario(self, nome, funcao, salario):
        funcionario = {"nome": nome, "funcao": funcao, "salario": salario}
        self.funcionarios.append(funcionario)

    def adicionar_quarto(self, numero_quarto, capacidade):
        quarto = {"numero_quarto": numero_quarto, "capacidade": capacidade, "reservado": False}
        self.quartos.append(quarto)

    def fazer_reserva(self, nome, numero_quarto, numero_hospedes):
        for quarto in self.quartos:
            if quarto["numero_quarto"] == numero_quarto and not quarto["reservado"]:
                quarto["reservado"] = True
                reserva = {"nome": nome, "numero_quarto": numero_quarto, "numero_hospedes": numero_hospedes}
                self.reservas.append(reserva)
                return f"Reserva feita para {nome} no quarto {numero_quarto}"
            return f"Quarto {numero_quarto} não está disponível" 

    def calcular_conta(self, nome):
        for reserva in self.reservas:
            if reserva["nome"] == nome:
                numero_quarto =  reserva["numero_quarto"]
                numero_hospedes = reserva["numeros_hospedes"]

                conta = numero_hospedes * 100
                return f"Conta para {nome} no quarto {numero_quarto}: {conta}"
            return f"Nenhuma reserva encontrada para {nome}"

    def exibir_funcionarios(self):
        for funcionario in self.funcionarios:
            print(f"Nome: {funcionario['nome']}, Função: {funcionario['funcao']}, Salário: {funcionario['salario']}")

    def exibir_quartos(self):
        for quarto in self.quartos:
            print(f"Numero do Quarto: {quarto['numero_quarto']}, Capacidade: {quarto['capacidade']}, Reservado: {quarto['reservado']}")

    def exibir_reservas(self):
        for reserva in self.reservas:
            print(f"Nome: {reserva['nome']}, Numero do Quarto: {reserva['numero_quarto']}, Num Hospedes: {reserva['num_hospedes']}")

hotel =  Hotel("Grand Hotel")

while True:
    print("\nMenu do Hotel:")
    print("1. Adicionar Funcionário")
    print("2. Adicionar Quarto")
    print("3. Fazer Reserva")
    print("4. Calcular Conta")
    print("5. Exibir Funcionários")
    print("6. Exibir Quartos")
    print("7. Exibir Reservas")
    print("8. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome do funcionário: ")
        funcao = input("Digite a função do funcionário: ")
        salario = input("Digite o salário do funcionário: ")
        hotel.adicionar_funcionario(nome, funcao, salario)
        print(f"Funcionário {nome} adicionado com sucesso!")

    elif escolha == "2":
        numero_quarto = int(input("Digite o número do quarto: "))
        capacidade = int(input("Digite a capacidade do quarto: "))
        hotel.adicionar_quarto(numero_quarto, capacidade)
        print(f"Quarto {numero_quarto} adicionado com sucesso!")

    elif escolha == "3":
        nome = input("Digite o nome do hóspede: ")
        numero_quarto = int(input("Digite o número do quarto: "))
        num_hospedes = int(input("Digite o número de hóspedes: "))
        print(hotel.fazer_reserva(nome, numero_quarto, num_hospedes)) 

    elif escolha == "4":
        nome = input("Digite o nome do hóspede: ")
        print(hotel.calcular_conta(nome))

    elif escolha == "5":
        hotel.exibir_funcionarios()

    elif escolha == "6":
        hotel.exibir_quartos()

    elif escolha == "7":
        hotel.exibir_reservas()

    elif escolha == "8":
        print("Até mais")
        break

    else:
        print("Escolha inválida. Por favor, tente novamente.")                        