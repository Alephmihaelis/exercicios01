
class Animal:

    def __init__(self):

        self.especie = ''
        self.genero = ''
        self.subespecie = ''

# Encapsulamento com getter e setter

    # SETTERS -> Define os valores dos atributos encapsulados
    def setEspecie(self, especie):
        self.especie = especie.strip()
    
    def setGenero(self, genero):
        self.genero = genero.strip()

    def setSubespecie(self, subespecie):
        self.subespecie = subespecie.strip()

    # GETTERS -> Lê os valores dos atributos encapsulados.

    def getEspecie(self):
        if self.especie != '':
            return self.especie
        else:
            return 'Erro ao mostrar espécie.'

    def getGenero(self):
        if self.genero != '':
            return self.genero
        else:
           return 'Erro ao mostrar gênero.'

    def getSubespecie(self):
        if self.subespecie != '':
            return self.subespecie
        else:
            return 'Erro ao mostrar subespécie.'

minhoca = Animal()
minhoca.setEspecie('Taturana')
print(minhoca.getEspecie())


minhoca.especie = '           taturanada            ' # Exemplo de acesso direto ao atributo
print(minhoca.especie) # Exemplo de acesso direto ao atributo