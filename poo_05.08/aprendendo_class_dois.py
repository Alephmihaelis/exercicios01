
produtos = ['iPhone', 'AirPod', 'iPad'] # Esse comando cria uma lista de produtos (observa os [])

class ControleRemoto():
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar canal...')
        elif botao == '-':
            print('Diminuir canal...')


controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')

controle_remoto.passar_canal('+')
controle_remoto2.passar_canal('-')

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido.')
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido.')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print(f'Faça upgrade para premium para ver esse filme')
        else:
            print('Plano inválido.')

cliente_um = Cliente('Lira', 'lira@gmail.com', 'basic')
cliente_dois = Cliente('João', 'joão@gmail.com', 'premium')

print(cliente_um.plano)
print(cliente_um.plano)
cliente_um.mudar_plano('blablabla')
print(cliente_um.plano)
cliente_um.ver_filme('harry potter', 'premium')
cliente_um.mudar_plano('premium')
cliente_um.ver_filme('harry potter', 'premium')