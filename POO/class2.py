class pessoa:
    def __init__(self, nome, idade, peso, genero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.genero = genero

minha_pessoa = pessoa("Jorge", 20, 54, "masculino")
print(minha_pessoa.nome, minha_pessoa.idade, minha_pessoa.peso, minha_pessoa.genero)

