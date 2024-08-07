
class Carro:

    # Método construtor
    def __init__(self, cor, marca, modelo):

        # Cores possíveis do carro
        cores = {'preto', 'branco', 'vermelho', 'azul'}

        # Atributos do carro
        self.cor = ''
        self.marca = ''
        self.modelo = ''
        # Testa cor
        if cor in cores: # Essa linha dá segurança ao código. Só entrará a cor que constar na variável cores. 
            self.cor = cor
        else:
            print('Vai te catar!')

    # Métodos
    def ligar(self):
        print('Vrum, vrum')
    
    def desligar(self):
        print('Cof, cof')

# Cria um objeto 'fuscao'
fuscao = Carro('carro', 'VW', '1800') # O nome técnico disso é INSTÂNCIA do tipo Carro

# Ligar o carro
fuscao.ligar()

# Desligar o carro
fuscao.desligar()

# Ler a cor do carro
print(fuscao.cor) # Não se deve nunca ler diretamente um atributo de uma classe.

'''
# Cria outro objeto
opalao = Carro() # Instância da classe 'Carro'
opalao.cor = 'vermelho' # Define o valor do atributo 'cor'
opalao.ligar() # Executa o método 'ligar' sobre 'opalao'
print(opalao.cor) # Mostra a cor de 'opalao'
opalao.desligar() # Executa o método 'desligar' sobre 'opalao'
'''