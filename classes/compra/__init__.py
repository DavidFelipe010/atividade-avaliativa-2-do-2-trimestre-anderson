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
        self.pg = False

    def __str__(self):
        return f'{self.id}/{self.produto.id}/{self.cliente}'

    def realizar_pagamento(self, qtd_produtos):
        self.qtd_produtos = qtd_produtos

        if self.pg:
            print(f'| Você {texto.cores('vermelho')}não{texto.cores()} pode realizar a mesma compra duas vezes!')

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return
        
        elif self.qtd_produtos > self.produto.estoque:
            print(f'| {texto.cores('amarelo')}A quantidade de compra é maior que o estoque! {texto.cores()}{texto.cores('vermelho')}Não{texto.cores()}{texto.cores('amarelo')} foi possível realizar a compra!{texto.cores()}')

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return
        
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
            self.pg = True

            print(f'| {texto.cores('verde')}Compra realizada com sucesso!{texto.cores()}')
            
            self.produto.estoque -= qtd_produtos
        
        else:
            print(f'| {texto.cores('vermelho')}Compra cancelada!{texto.cores()}')


        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
        return

    def emitir_nota_fiscal(self):
        if not self.pg:
            print(f'| {texto.cores('amarelo')}A compra ainda {texto.cores() + texto.cores('vermelho')}não{texto.cores() + texto.cores('amarelo')} foi paga!{texto.cores()}')
            
            return
        
        nome_mercado = 'David & Rohan mercados'
        linha = '='
        
        return f'''{linha * 80} {nome_mercado} {linha * 80}
Data da compra: {self.data}       
Produto: {self.produto.nome} {self.qtd_produtos}x
Subtotal: R${self.produto.preco:,.2f}
{linha * 184} 
Valor total: R${self.produto.preco * self.qtd_produtos:,.2f}
{linha * 184}'''        