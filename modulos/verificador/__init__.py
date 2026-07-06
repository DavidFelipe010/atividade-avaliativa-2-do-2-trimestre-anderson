from modulos.texto import *

texto = Texto()

class Verificadores:
    def verifica_bool(self, txt):
        while True:
            label = input(txt).strip().lower()

            if not label in 'sn' or not label:
                continue
            else:
                label = label[0]

            if label == 's':
                return True
            
            return False
        

    def verifica_nums_naturais(self, txt):
        while True:
            label = input(txt).strip()

            try:
                num = int(label)

                if num < 0:
                    print(f'{texto.cores('vermelho')}[ERROR] Digite apenas números maiores que {texto.cores()}{texto.cores('amarelo')}0{texto.cores()}{texto.cores('vermelho')}!{texto.cores()}\n')
                    continue

                return num

            except (TypeError, ValueError):
                print(f'{texto.cores('vermelho')}[ERROR] Digite apenas números naturais!\n{texto.cores()}')

    def verifica_int(self, txt):
        while True:
            label = input(txt).strip()

            try:
                num = int(label)

                return num

            except (TypeError, ValueError):
                print(f'{texto.cores('vermelho')}[ERROR] Digite apenas números inteiros!\n{texto.cores()}')
    
    def verifica_float(self, txt):
        while True:
            label = input(txt).strip().replace(',','.')

            try:
                num = float(label)

                return num

            except (TypeError, ValueError):
                print(f'{texto.cores('vermelho')}[ERROR] Digite apenas números!\n{texto.cores()}')
