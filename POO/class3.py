class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"Funcionário: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario:.2f}"

class CadastroFuncionarios:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo, salario):
        novo_funcionario = Funcionario(nome, cargo, salario)
        self.funcionarios.append(novo_funcionario)

    def remover_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f"Funcionário {nome} removido com sucesso!")
                return
        print(f"Funcionário {nome} não encontrado.")

    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

def main():
    cadastro = CadastroFuncionarios()

    while True:
        print("\nMenu:")
        print("1. Adicionar Funcionário")
        print("2. Remover Funcionário")
        print("3. Listar funcionário")
        print("4. Sair.")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do Funcionário: ")
            cargo = input("Digite o cargo do Funcionário: ")  
            salario = float(input("Digite o salário do Funcionário: "))
            cadastro.adicionar_funcionario(nome, cargo, salario)
        elif opcao == "2":
            nome = input("Digite o nome do Funcionário a ser removido: ")
            cadastro.remover_funcionario(nome)
        elif opcao == "3":
            cadastro.listar_funcionarios()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()