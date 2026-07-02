from classes.cliente import *
from classes.compra import *
from classes.produto import *
from modulos.texto import *
from modulos.operacoes_classes import *
from modulos.texto import *

produtos = []
compras = []

texto = Texto()
operacoes = Operacoes()

while True:
    texto.limpa()
    texto.titulo('menu')

    print('''O que você gostaria de fazer? 

[ 0 ] - Encerrar programa
[ 1 ] - Cadastrar Produto
[ 2 ] - Cadastrar Cliente
[ 3 ] - Listar Produtos
[ 4 ] - Cadastrar Compra
[ 5 ] - Realizar pagamento''')
    opcao = int(input('Sua opção: '))
    
    match opcao:
        case 0:
            texto.limpa()
            print(f'| {texto.cores('verde')}Obrigado por usar o nosso sistema!{texto.cores()}')
            break

        case 1:
            produto = operacoes.cadastrar_produto(classe=Produto)
            produtos.append(produto)
        
        case 2:
            cliente = operacoes.cadastrar_cliente(classe=Cliente)
        
        case 3:
            operacoes.listar_produtos(lst=produtos)
        
        case 4:
            try:
                compra = operacoes.cadastrar_compra(classe=Compra, cliente=cliente, lst_produtos=produtos)
                compras.append(compra)
            
            except NameError:
                texto.limpa()
                print(f'| {texto.cores('amarelo')}Não há nenhum cliente cadastrado!{texto.cores()}')

                input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

        case 5:
            operacoes.realizar_compra(lst=compras)
        
        case _:
            print('Informe um número válido!')