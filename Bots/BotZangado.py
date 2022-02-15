from Bots.Bot import Bot
from Bots.comando import Comando

comandos = Comando(1, "conte uma pidada", ["hehe piada1", "hehe piada2", "PIADA3"])


class BotZangado(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [comandos]
 
    @property
    def nome(self):
        return self.__nome  
    
    @property
    def comandos(self):
        return self.__comandos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "sou o zangado"
 
    def mostra_comandos(self):
        mensa = ""
        for i in self.__comandos:
            mensa +=  f"{i.id} --- {i.mensagem}/n"
        return mensa
    
    def executa_comando(self,cmd):
        for i in self.__comandos:
            if i.id == cmd:
                resposta = i.get_resposta_random()
                return resposta
        return 'Comando não encontrado'
        

    def boas_vindas(self):
        return 'AHHH nao seja bem vindo, o que voce quer?'

    def despedida(self):
        return 'vai tarde'