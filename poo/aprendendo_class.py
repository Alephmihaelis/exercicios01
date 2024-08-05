
class Carro:

    # Método construtor
    def __init__(self):

        # Atributos
        self.cor = ''
        self.marca = ''
        self.modelo = ''
        pass

    # Métodos
    def ligar(self):
        print('Vrum, vrum')
    
    def desligar(self):
        print('Cof, cof')

# Cria um objeto 'fuscao'
fuscao = Carro() # O nome técnico disso é INSTÂNCIA do tipo Carro

# Cor do fuscão
fuscao.cor = 'Preto'

# Ligar o carro
fuscao.ligar()

# Desligar o carro
fuscao.desligar()

# Ler a cor do carro
print(fuscao.cor)


# Cria outro objeto
opalao = Carro()
opalao.cor = 'vermelho'
opalao.ligar()
print(opalao.cor)
opalao.desligar()
