
class VeículoMotor:

    def __init__(self, minhaMarca, meuModelo):

        self.marca = minhaMarca
        self.modelo = meuModelo

    def ligar(self, barulho = 'Vrum, vrum!'):
        print('Ligando com', barulho)
    
    def desligar(self, barulho = 'Cof! Cof!'):
        print('Desligando com', barulho)

class Motoca(VeículoMotor):

    qtdRodas = 2

    def ligar(self, grau):
        print(grau, 'Tibum!')

class Carreta(VeículoMotor):

    qtdRodas = 12
    capacidade = 8000

# Instância de Motoca

hondinha = Motoca('Honda', 'CG125')
hondinha.ligar('Tuim! Tuim!')
print(hondinha.qtdRodas) # Manusear atributos diretamente é perigoso, porque se pode pôr nele valores incorretos.
print('--------------------')

# Instância de Carreta

scanao = Carreta('Scania', 'RSRR3200')
scanao.ligar('Brão! Brão!')
print(scanao.qtdRodas)