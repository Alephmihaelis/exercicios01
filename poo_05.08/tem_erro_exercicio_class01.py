
import re

class User:

    def __init__(self):

        self.__id = 0
        self.__name = ''
        self.__email = ''
        self.__password = ''

    # Método que valida e-mails usando Regex
    # https://www.catabits.com.br/view/regex_para_validar_emails
    # regexr.com

#    def validate_email(self, email):
        # Regex para validar endereços de e-mail, usada pelo HTML5
        # OBS: deve estar em uma única linha
#pattern = r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?)*$'
    # Verifica se o e-mail corresponde ao padrão regex
#if re.match(pattern, email):
#    return True
#else:
#    return False        
#    self.__email = email

    def setId(self, id):
        # tratamentos, filtros, sanitização e validação
        self.__id = int(id) # força a conversão do Id para integer
  
    def setName(self, name):
        # tratamentos, filtros, sanitização e validação
        self.__name = name.strip()

    def setEmail(self, email):
        # tratamentos, filtros, sanitização e validação
#        if self.validate_email(email):
        self.__email = email.strip()
#        else:
#            print('Erro! Endereço de e-mail inválido')

    def setPassword (self, password):
        self.__password = password
    
    def getId(self):
        return self.__id
    def getName(self):
        return self.__name
    def getEmail(self):
        return self.__email
    def getPassword(self):
        return self.__password

