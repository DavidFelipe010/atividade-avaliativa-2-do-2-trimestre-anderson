class Produto:
    def __init__(self, id, nome, preco, quantidade, validade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.validade = validade

    def __str__(self):
        return f'{self.id}/{self.nome}/{self.validade}'
    
    def mostrar_preco(self):
        return f'R${self.preco:,.2f}'

    def mostrar_quantidade_estoque(self):
        return f'{self.quantidade} unidades'
        