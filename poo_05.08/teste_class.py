
class PersonagensGC:

    def __init__(self, nome, corprincipal, classes, nome_classes):

        self.nome = nome
        self.corprincipal = corprincipal
        self.classes = classes
        self.nome_classes = nome_classes

elesis = PersonagensGC('Elesis', 'vermelho', '4', 'Espadachim, Cavaleira, Gladiadora, Justiceira')
print(elesis.nome)

lire = PersonagensGC('Lire', 'amarelo', '4', 'Arqueira, Caçadora, Guardiã, Nova')
print(lire.nome_classes)

arme = PersonagensGC('Arme', 'roxo', '4', 'Maga, Alquimista, Feiticeira, Arquimaga')
print(arme.nome)

lass = PersonagensGC('Lass', 'azul', '4', 'Ninja, Mercenário, Vingador, Retalhador')
print(lass.nome, lass.corprincipal, lass.classes, lass.nome_classes)