
class User():

    def __init__(self):

        self.__id = int('')
        self.__name = ''
        self.__email = ''
        self.__password = ''
    
    def setId(self, id):
        self.__id = id
    
    def setName(self, name):
        self.__name = name
    
    def setEmail(self, email):
        self.__email = email

    def setPassword(self, password):
        self.__password = password

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPassword(self):
        return self.__password

    def new(self, id, name):
        pass
    
    def view(self, id):
        pass
    
    def delete(self, id):
        pass



class Student(User):

    def __init__(self):
        super().__init__()

        self.__notas = ()
        self.__presenca = ()
        self.__curso = ''

    def setNotas(self, notas):
        pass

    def setPresenca(self, presenca):
        pass

    def setCurso(self, curso):
        pass

    def getNotas(self):
        return self.__notas

    def getPresenca(self):
        return self.__presenca

    def getCurso(self):
        return self.__curso