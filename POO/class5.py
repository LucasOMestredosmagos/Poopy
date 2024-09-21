class Fatura:
    def __init__(self, nome_do_item, preco_unitario, quantidade):
        self.nome_do_item = nome_do_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade
        return self.valor_total

minha_fatura = Fatura("Videogame", 5200, 2)
print(minha_fatura.nome_do_item, minha_fatura.preco_unitario, minha_fatura.quantidade, minha_fatura.valor_total)

minha_fatura.gerar_fatura()
print(minha_fatura.valor_total)