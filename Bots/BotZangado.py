from Bots.Bot import Bot
from comando import Comando

piada = Comando(1, "conte uma pidada", ["lista de piadas"])


class BotZangado(Bot):
    def __init__(self,nome, Comandos:list ):
        self.__nome = nome
        self.__comandos = Comandos
 
    @property
    def nome(self):
        return self.__nome  

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "sou o zangado"
 
    def mostra_comandos(self):
        mensa = ""
        for i in self.__comandos:
            mensa +=  f"{i.id}--- {i.mensagem}/n"
        return mensa
    
    def executa_comando(self,cmd):
        for i in self.__comandos:
            if i.id == cmd:
                resposta = i.get_resposta_random()
        return resposta

    def boas_vindas(self):
        return 'AHHH nao seja bem vindo, o que voce quer?'

    def despedida(self):
        return 'vai tarde'