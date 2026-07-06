from classes.cliente import *
from classes.compra import *
from classes.produto import *
from modulos.texto import *
from modulos.operacoes_classes import *
from modulos.texto import *
from modulos.verificador import *

produtos = []
compras = []

texto = Texto()
operacoes = Operacoes()
verificadores = Verificadores()

while True:
    texto.limpa()
    texto.titulo('menu')

    print('''O que você gostaria de fazer? 
Obs.: Siga a ordem abaixo (Ignore o 0 e o listar produtos se quiser)

====== Parte 1 ======
[ 0 ] - Encerrar programa
[ 1 ] - Cadastrar Produto
[ 2 ] - Cadastrar Cliente
[ 3 ] - Cliente ir até o mercado
[ 4 ] - Listar Produtos
[ 5 ] - Cadastrar Compra
[ 6 ] - Realizar pagamento
[ 7 ] - Emitir nota fiscal
[ 8 ] - Cliente voltar para casa

====== Parte 2 ======
[ 9 ]  - Mostrar preço do produto
[ 10 ] - Mostar estoque do produto''')
    opcao = verificadores.verifica_int('Sua opção: ')
    
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
            texto.limpa()
            print(cliente.ir_ao_mercado())

            input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
        
        case 4:
            operacoes.listar_produtos(lst=produtos)
        
        case 5:
            try:
                compra = operacoes.cadastrar_compra(classe=Compra, cliente=cliente, lst_produtos=produtos)
                compras.append(compra)
            
            except NameError:
                texto.limpa()
                print(f'| {texto.cores('amarelo')}Não há nenhum cliente cadastrado!{texto.cores()}')

                input(f'\n| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')

        case 6:
            operacoes.realizar_compra(lst=compras)

        case 7:
            operacoes.emitir_nota_fiscal(lst=compras)

        case 8:
            texto.limpa()
            print(cliente.voltar_para_casa())

            input(f'| Pressione {texto.cores('amarelo')}ENTER{texto.cores()} para continuar...')
        
        
        case _:
            print('Informe um número válido!')
