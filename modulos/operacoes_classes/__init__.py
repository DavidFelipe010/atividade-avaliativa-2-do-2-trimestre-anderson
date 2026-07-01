import itertools
import datetime
from random import choice

# Iterator global que gera IDs automaticamente (0, 1, 2, 3, ...)
_id_counter_cliente = itertools.count(start=1, step=1)
_id_counter_produto = itertools.count(start=1, step=1)
_id_counter_compra = itertools.count(start=1, step=1)

def gerar_id_cliente():
    """
    Retorna um ID numérico incremental seguro e único.
    """
    try:
        return next(_id_counter_cliente)
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar ID: {e}")

def gerar_id_produto():
    """
    Retorna um ID numérico incremental seguro e único.
    """
    try:
        return next(_id_counter_produto)
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar ID: {e}")

def gerar_id_compra():
    """
    Retorna um ID numérico incremental seguro e único.
    """
    try:
        return next(_id_counter_compra)
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar ID: {e}")


def gerar_numero_protocolo():
    nums = (0,1,2,3,4,5,6,7,8,9)
    protocolo = ''
    for i in range(16):
        protocolo += f'{choice(nums)}'

    return protocolo


class Operacoes:
    def cadastrar_produto(self, classe):
        id = gerar_id_produto()
        nome = input('Qual o nome do produto: ')
        preco = float(input('Qual o preco do produto: '))
        quantidade = int(input('Quantos você deseja cadastrar: '))
        data_validade = input('Informe a data de validade do produto: ')

        return classe(id,nome,preco,quantidade,data_validade)
    
    def cadastrar_cliente(self, classe):
        #  id, nome, cpf, email, rg, data_nascimento
        id = gerar_id_cliente()
        nome = input('Qual o nome do Cliente: ')
        cpf = input('Qual o CPF do Cliente: ')
        email = input('Qual o Email do Cliente: ')
        rg = input('Qual o RG do Cliente: ')
        data_nascimento = input('Qual a data de nascimento do Cliente? Ex.: 03/03/2027: ')

        return classe(id,nome,cpf,email,rg,data_nascimento)

    def listar_produtos(self, lst):
        print(f'{"Id.":<10} {"Nome.":<25} {"Preço.":<10}')
        print('=' * 180)

        for produto in lst:
            preco = f'R${produto.preco}'
            print(f'{produto.id:<10} {produto.nome:<25} {preco:<10}')
    
    def cadastrar_compra(self, classe, cliente, lst_produtos):
        # id, data, numero_protocolo, produto
        id = gerar_id_compra()
        data = datetime.date.today()
        numero_protocolo = gerar_numero_protocolo()
        
        self.listar_produtos(lst_produtos)
        opc = int(input('Qual produto você quer cadastar na compra? (id): '))
        
        while not 1 <= opc <= len(lst_produtos):
            print('Esse id não existe!')
            opc = int(input('Qual produto você quer cadastar na compra? (id): '))

        produto = lst_produtos[opc - 1]

        return classe(id, data, numero_protocolo, produto, cliente)

    def listar_compras(self, lst):
        print(f'{"Id.":<10} {"Nome Produto.":<25}')
        print('=' * 180)

        for compra in lst:
            print(f'{compra.id:<10} {compra.produto.nome:<25}')

    def realizar_compra(self, lst):
        self.listar_compras(lst)
        opc = int(input('Qual comprar você quer realizar? (id):'))
        while not 1 <= opc <= len(lst):
            print('Esse ID não existe!')
            opc = int(input('Qual comprar você quer realizar? (id):'))

        compra = lst[opc - 1]

        qtd_compra = int(input('Quantos items você quer comprar?: '))

        compra.realizar_pagamento(qtd_compra)