class Produto:
    def __init__(self, id, nome, preco, estoque, validade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.validade = validade

    def __str__(self):
        return f'{self.id}/{self.nome}/{self.validade}'
    
    def mostrar_validade(self):
        return f'{self.validade}'

    def repor_estoque(self, qtd):
        self.estoque += qtd
        