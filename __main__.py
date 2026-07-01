from classes.cliente import *
from classes.compra import *
from classes.produto import *
from modulos.texto import *
from modulos.operacoes_classes import *

produtos = []
compras = []
operacoes = Operacoes()

while True:
    print('-=' * 20,end=' ')
    print('MENU',end=' ')
    print('=-' * 20)

    print('O que você gostaria de fazer? ')
    opcao = int(input('''[ 1 ] - Cadastrar Produto
[ 2 ] - Cadastrar Cliente
[ 3 ] - Listar Produtos
[ 4 ] - Cadastrar comprar
[ 5 ] - Realizar pagamento
Sua opção: '''))
    match opcao:
        case 1:
            produto = operacoes.cadastrar_produto(classe=Produto)
            print(produto)
            produtos.append(produto)
        case 2:
            cliente = operacoes.cadastrar_cliente(classe=Cliente)
            print(cliente)
        case 3:
            operacoes.listar_produtos(produtos)
        case 4:
            compra = operacoes.cadastrar_compra(classe=Compra, cliente=cliente, lst_produtos=produtos)
            compras.append(compra)
        case 5:
            operacoes.realizar_compra(compras)
        case _:
            print('Informe um número válido')