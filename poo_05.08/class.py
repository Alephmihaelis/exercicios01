
class User:

    def __init__(self):

        self.__id__ = ''
        self.__name__ = ''
        self.__email__ = ''
        self.__password__ = ''
    
    def setId(self, id):
        self.__id__ = id
    
    def setName(self, name):
        self.__name__ = name
    
    def setEmail(self, email):
        self.__email__ = email

    def setPassword(self, password):
        self.__password__ = password

    def getId(self):
        return self.__id__

    def getName(self):
        return self.__name__

    def getEmail(self):
        return self.__email__

    def getPassword(self):
        return self.__password__

    def new(self, id, name):
        pass
    
    def view(self, id):
        pass
    
    def delete(self, id):
        pass


class Student(User):

    def __init__(self):
        super().__init__()

        self.__notas__ = ()
        self.__presenca__ = ()
        self.__curso__ = ''

    def setNotas(self, notas):
        pass

    def setPresenca(self, presenca):
        pass

    def setCurso(self, curso):
        pass

    def getNotas(self):
        return self.__notas__

    def getPresenca(self):
        return self.__presenca__

    def getCurso(self):
        return self.__curso__