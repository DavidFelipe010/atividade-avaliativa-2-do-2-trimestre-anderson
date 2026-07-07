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
        data_validade = verificadores.verifica_data('| Informe a data de validade do produto? (Ex.: 03/02/2027): ')

        texto.limpa()

        print(f'|{texto.cores('verde')} Cadastro de {texto.cores()}{texto.cores('amarelo')}produto{texto.cores()}{texto.cores('verde')} realizado com sucesso!{texto.cores()}')

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

        return classe(id, nome.title(), preco, quantidade, texto.formatar_data(data_validade))
    
    def cadastrar_cliente(self, classe, cliente):
        texto.limpa()
        texto.titulo('cadastar cliente')
        
        if cliente is not None:
            print(f'| {texto.cores('vermelho')}Não{texto.cores()} pode cadastar mais de 1 cliente!')

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
            
            return cliente
        
        id = gerar_id_cliente()
        
        nome = input('| Qual o nome do Cliente? (Ex.: João Neto): ')
        cpf = verificadores.verifica_cpf('| Qual o CPF do Cliente? (Ex.:999.999.999-00): ')
        email = input('| Qual o Email do Cliente? (Ex.: joaoneto@gmail.com): ')
        rg = verificadores.verifica_rg('| Qual o RG do Cliente? (Ex.: 99.999.999): ')
        data_nascimento = verificadores.verifica_data('| Qual a data de nascimento do Cliente? (Ex.: 03/03/1994): ')

        texto.limpa()

        print(f'\n| {texto.cores('verde')}Cadastro de {texto.cores()}{texto.cores('amarelo')}cliente{texto.cores()}{texto.cores('verde')} realizado com sucesso!{texto.cores()}')

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
        
        return classe(id, nome.title(), texto.formatar_cpf(cpf), email, texto.formatar_rg(rg), texto.formatar_data(data_nascimento))

    def listar_produtos(self, lst):
        texto.limpa()
        texto.titulo('lista de produtos')

        if not lst:
            print(f'| {texto.cores('amarelo')} Não há nenhum produto cadastrado!{texto.cores()}')
        
        else:       
            texto.linha(70)
            print(f'{"Id.":<10} {"Nome.":<25} {"Preço.":<10} {"Estoque."}')
            texto.linha(70)

            for produto in lst:
                preco = f'R${produto.preco:,.2f}'
                
                print(f'{produto.id:<10} {produto.nome:<25} {preco:<10} {produto.estoque}')
            texto.linha(70)

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

        return
    
    def lista_produtos(self, lst):        
            texto.linha(70)
            print(f'{"Id.":<10} {"Nome.":<25} {"Preço.":<10} {"Estoque."}')
            texto.linha(70)

            for produto in lst:
                preco = f'R${produto.preco:,.2f}'
                
                print(f'{produto.id:<10} {produto.nome:<25} {preco:<10} {produto.estoque}')
            texto.linha(70)

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
            opc = verificadores.verifica_int('| Qual produto você quer cadastrar na compra? (id): ')
            
            while not 1 <= opc <= len(lst_produtos):
                print(f'\n| Esse {texto.cores('amarelo')}ID{texto.cores()} {texto.cores('vermelho')}não existe{texto.cores()}!')
                opc = verificadores.verifica_int('| Qual produto você quer cadastrar na compra? (id): ')
            
            produto = lst_produtos[opc - 1]
            
            texto.limpa()
            
            print(f'| {texto.cores('verde')} Compra cadastrada com sucesso!{texto.cores()}')
            
            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
            
            return classe(id, data, numero_protocolo, produto, cliente)

    def listar_compras(self, lst):
        texto.linha(60)
        print(f'{"Id.":<10} {"Nome Produto.":<25} {"Pago."}')
        texto.linha(60)

        for compra in lst:
            pg = compra.pg
            txt_pg = '✅' if pg else '❌'

            print(f'{compra.id:<10} {compra.produto.nome:<25} {txt_pg}')
        texto.linha(60)

    def realizar_compra(self, lst):
        texto.limpa()
        texto.titulo('realizar compra')
        
        if not lst:
            print(f'| {texto.cores('amarelo')}Não há nenhuma compra cadastrada!{texto.cores()}')

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return

        
        self.listar_compras(lst)

        opc = verificadores.verifica_int('| Qual comprar você quer realizar? (id): ')
            
        while not 1 <= opc <= len(lst):
            print(f'\n| Esse {texto.cores('amarelo')}ID{texto.cores()} {texto.cores('vermelho')}não existe{texto.cores()}!')
            opc = verificadores.verifica_int('| Qual comprar você quer realizar? (id): ')

        compra = lst[opc - 1]

        if not compra.pg:
            texto.limpa()
            self.qtd_compra = verificadores.verifica_int('| Quantos itens você quer comprar? (unidades): ')

        texto.limpa()
        compra.realizar_pagamento(self.qtd_compra)

    def emitir_nota_fiscal(self, lst):
        texto.limpa()
        texto.titulo('Emitir nota fiscal')

        if not lst:
            print(f'| {texto.cores('amarelo')}Não há nenhuma compra cadastrada!{texto.cores()}')

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return
            
        self.listar_compras(lst)

        opc = verificadores.verifica_int('| Qual comprar você quer emitir nota fiscal? (id): ')
            
        while not 1 <= opc <= len(lst):
            print(f'\n| Esse {texto.cores('amarelo')}ID{texto.cores()} {texto.cores('vermelho')}não existe{texto.cores()}!')
            opc = verificadores.verifica_int('| Qual comprar você quer nota fiscal? (id): ')

        compra = lst[opc - 1]

        texto.limpa()
        print(compra.emitir_nota_fiscal())

        input(f'| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

    def mostar_validade(self, lst):
        texto.limpa()
        texto.titulo('mostar validade do produto')
       
        if not lst:
            print(f'| {texto.cores('amarelo')} Não há nenhum produto cadastrado!{texto.cores()}')
            
            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return
       
        self.lista_produtos(lst)
        opc = verificadores.verifica_int('| Qual produto você quer verificar a validade? (id): ')
            
        while not 1 <= opc <= len(lst):
            print(f'\n| Esse {texto.cores('amarelo')}ID{texto.cores()} {texto.cores('vermelho')}não existe{texto.cores()}!')
            opc = verificadores.verifica_int('| Qual produto você quer verificar a validade? (id): ')
            
        produto = lst[opc - 1]

        texto.limpa()

        print(f'| {produto.mostrar_validade()}')

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

        return
    
    def repor_estoque(self, lst):
        texto.limpa()
        texto.titulo('repor estoque')
       
        if not lst:
            print(f'| {texto.cores('amarelo')} Não há nenhum produto cadastrado!{texto.cores()}')
            
            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

            return
       
        self.lista_produtos(lst)
        opc = verificadores.verifica_int('| Qual produto você quer repor o estoque? (id): ')
            
        while not 1 <= opc <= len(lst):
            print(f'\n| Esse {texto.cores('amarelo')}ID{texto.cores()} {texto.cores('vermelho')}não existe{texto.cores()}!')
            opc = verificadores.verifica_int('| Qual produto você quer repor o estoque? (id): ')
            
        produto = lst[opc - 1]

        texto.limpa()

        qtd_reposicao = verificadores.verifica_int(f'| Quanto você quer repor no estoque? (unidades): ')

        texto.limpa()

        produto.repor_estoque(qtd_reposicao)

        print(f'| Reposição feita com {texto.cores('verde')}sucesso{texto.cores()}!')

        input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

