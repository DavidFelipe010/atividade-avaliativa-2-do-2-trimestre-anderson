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

    def formatar_cpf(self, cpf):
        return f'{cpf[:4]}.{cpf[4:7]}.{cpf[7:9]}-{10:}'

    def formatar_data(self, data):
        return f'{data[:2]}/{data[2:4]}/{data[4:]}'
    
    def formatar_rg(self, rg):
        return f'{rg[:2]}.{rg[2:5]}.{rg[5:]}'
