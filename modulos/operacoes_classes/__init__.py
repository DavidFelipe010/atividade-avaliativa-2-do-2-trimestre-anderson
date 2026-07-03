import itertools
import datetime
from random import choice
from modulos.texto import Texto
from modulos.verificador import *

texto = Texto()
verificadores = Verificadores()

id_counter_cliente = itertools.count(start=1, step=1)
id_counter_produto = itertools.count(start=1, step=1)
id_counter_compra = itertools.count(start=1, step=1)


def gerar_id_cliente():
    try:
        return next(id_counter_cliente)
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar ID: {e}")


def gerar_id_produto():
    try:
        return next(id_counter_produto)
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar ID: {e}")


def gerar_id_compra():
    try:
        return next(id_counter_compra)
    except Exception as e:
        raise RuntimeError(f"Erro ao gerar ID: {e}")


def gerar_numero_protocolo():
    nums = (0,1,2,3,4,5,6,7,8,9)
    protocolo = ''
    
    for _ in range(16):
        protocolo += f'{choice(nums)}'

    return protocolo


class Operacoes:
    def cadastrar_produto(self, classe):
        texto.limpa()
        texto.titulo('cadastar produto')

        id = gerar_id_produto()
        nome = input('| Qual o nome do produto: ')
        preco = verificadores.verifica_float('| Qual o preco do produto? R$')
        quantidade = verificadores.verifica_int('| Qual estoque? (unidades): ')
        data_validade = input('| Informe a data de validade do produto? (Ex.: 03/02/2027): ').replace('\\','').replace('/','')

        texto.limpa()

        print(f'|{texto.cores('verde')} Cadastro de {texto.cores()}{texto.cores('amarelo')}produto{texto.cores()}{texto.cores('verde')} realizado com sucesso!{texto.cores()}')

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

        return classe(id,nome,preco,quantidade,data_validade)
    
    def cadastrar_cliente(self, classe):
        texto.limpa()
        texto.titulo('cadastar cliente')
        


        id = gerar_id_cliente()
        
        if id > 1:
            print(f'| {texto.cores('vermelho')}Não{texto.cores()} pode cadastar mais de 1 cliente!')

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
            
            return 
        
        nome = input('| Qual o nome do Cliente? (Ex.: João Neto): ')
        cpf = input('| Qual o CPF do Cliente? (Ex.:999.999.999-00): ').replace('.', '').replace('-', '')
        email = input('| Qual o Email do Cliente? (Ex.: joaoneto@gmail.com): ')
        rg = input('| Qual o RG do Cliente? (Ex.: 99.999.999): ').replace('.','')
        data_nascimento = input('| Qual a data de nascimento do Cliente? (Ex.: 03/03/2027): ').replace('\\', '').replace('/', '')

        texto.limpa()

        print(f'\n| {texto.cores('verde')}Cadastro de {texto.cores()}{texto.cores('amarelo')}cliente{texto.cores()}{texto.cores('verde')} realizado com sucesso!{texto.cores()}')

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
        
        return classe(id,nome,cpf,email,rg,data_nascimento)

    def listar_produtos(self, lst):
        texto.limpa()
        texto.titulo('lista de produtos')

        if not lst:
            print(f'| {texto.cores('amarelo')} Não há nenhum produto cadastrado!{texto.cores()}')
        
        else:       
            texto.linha(60)
            print(f'{"Id.":<10} {"Nome.":<25} {"Preço.":<10}')
            texto.linha(60)

            for produto in lst:
                preco = f'R${produto.preco:,.2f}'
                
                print(f'{produto.id:<10} {produto.nome:<25} {preco:<10}')
            texto.linha(60)

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

        return
    
    def lista_produtos(self, lst):        
            texto.linha(60)
            print(f'{"Id.":<10} {"Nome.":<25} {"Preço.":<10}')
            texto.linha(60)

            for produto in lst:
                preco = f'R${produto.preco:,.2f}'
                
                print(f'{produto.id:<10} {produto.nome:<25} {preco:<10}')
            texto.linha(60)

    def cadastrar_compra(self, classe, cliente, lst_produtos):
        texto.limpa()
        texto.titulo('Cadastrar compra')

        if not lst_produtos:
            print(f'| {texto.cores('amarelo')} Não há nenhum produto cadastrado!{texto.cores()}')
            
            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return
            
        else:
            id = gerar_id_compra()
            data = datetime.date.today()
            numero_protocolo = gerar_numero_protocolo()
            
            self.lista_produtos(lst_produtos)
            opc = verificadores.verifica_int('| Qual produto você quer cadasar na compra? (id): ')
            
            while not 1 <= opc <= len(lst_produtos):
                print(f'\n| Esse {texto.cores('amarelo')}ID{texto.cores()} {texto.cores('vermelho')}não existe{texto.cores()}!')
                opc = verificadores.verifica_int('| Qual produto você quer cadasar na compra? (id): ')
            
            produto = lst_produtos[opc - 1]
            
            texto.limpa()
            
            print(f'| {texto.cores('verde')} Compra cadastrada com sucesso!{texto.cores()}')
            
            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
            
            return classe(id, data, numero_protocolo, produto, cliente)

    def listar_compras(self, lst):
        texto.linha(51)
        print(f'{"Id.":<10} {"Nome Produto.":<25}')
        texto.linha(51)

        for compra in lst:
            print(f'{compra.id:<10} {compra.produto.nome:<25}')
        texto.linha(51)

    def realizar_compra(self, lst):
        texto.limpa()
        texto.titulo('realizar compra')
        
        if not lst:
            print(f'| {texto.cores('amarelo')}Não há nenhuma compra cadastrada!{texto.cores()}')

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return

        else:
            self.listar_compras(lst)

            opc = verificadores.verifica_int('| Qual comprar você quer realiar? (id): ')
            
            while not 1 <= opc <= len(lst):
                print(f'\n| Esse {texto.cores('amarelo')}ID{texto.cores()} {texto.cores('vermelho')}não existe{texto.cores()}!')
                opc = verificadores.verifica_int('| Qual comprar você quer realiar? (id): ')

            compra = lst[opc - 1]

            texto.limpa()
            self.qtd_compra = verificadores.verifica_int('| Quantos itens você quer comprar? (unidades): ')

            texto.limpa()
            compra.realizar_pagamento(self.qtd_compra)

    def emitir_nota_fiscal(self, lst):
        self.listar_compras(lst)
