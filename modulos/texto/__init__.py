import os

class Texto:
    def limpa(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def titulo(self, txt):
        linha = '=' * (len(txt.strip()) + 16)

        print(f'''{linha}
        {txt.strip().title()}
{linha}''')
        
    def linha(self, qtd=80):
        print('=' * qtd)

    def cores(self, cor='normal'):
        dic_cores = {'normal':'\033[m',
                     'vermelho':'\033[31m',
                     'verde':'\033[32m',
                     'amarelo':'\033[33m',
                     'azul':'\033[34m'}
        
        return dic_cores[cor]
