from abc import ABC, abstractmethod

class EntradaESaidaDeArquivoDeMensagens(ABC):
    @abstractmethod
    def importar(self, titulo_do_arquivo_com_mensagens: str):
        pass

    @abstractmethod
    def exportar(self, mensagens: dict):
        pass

