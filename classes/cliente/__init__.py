
class Cliente:
    def __init__(self, id, nome, cpf, email, rg, data_nascimento):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.rg = rg
        self.data_nascimento = data_nascimento

    def __str__(self):
        return f'{self.id}/{self.nome}/{self.cpf}'
    
    def ir_ao_mercado(self):
        return f'{self.nome} está indo ao mercado...'
    
    def voltar_para_casa(self):
        return f'{self.nome} está voltando para casa, com suas compras...'