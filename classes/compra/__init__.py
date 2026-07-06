from modulos.verificador import Verificadores
from modulos.texto import Texto

texto = Texto()
verificadores = Verificadores()

class Compra:
    def __init__(self, id, data, numero_protocolo, produto, cliente):
        self.id = id
        self.data = data
        self.numero_protocolo = numero_protocolo
        self.produto = produto
        self.cliente = cliente.id

    def __str__(self):
        return f'{self.id}/{self.produto.id}/{self.cliente}'

    def realizar_pagamento(self, qtd_produtos):
        self.qtd_produtos = qtd_produtos
        print(f'''| Id da compra: {self.id}
| Número de protocolo: {self.numero_protocolo}
| Id do produto: {self.produto.id}
| Nome do produto: {self.produto.nome}
| Preço: R${self.produto.preco:,.2f}
| Quantidade: {self.qtd_produtos}x
| Total: R${(self.produto.preco * self.qtd_produtos):,.2f}
''')
        autorizar = verificadores.verifica_bool('| Quer realizar a compra? (S/N): ')

        texto.limpa()
        if autorizar:
            print(f'| {texto.cores('verde')}Compra realizada com sucesso!{texto.cores()}')
            
            self.produto.quantidade -= qtd_produtos
        else:
            print(f'| {texto.cores('vermelho')}Compra cancelada!{texto.cores()}')


        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
        return

    def emitir_nota_fiscal(self):
        nome_mercado = 'David & Rohan mercados'
        linha = '='
        
        return f'''{linha * 80} {nome_mercado} {linha * 80}
Produto: {self.produto.nome} {self.produto.quantidade}x
Subtotal: {self.produto.preco}
{linha * 184} 
Valor total: R${self.produto.preco * self.qtd_produtos:,.2f}
{linha * 184}'''        