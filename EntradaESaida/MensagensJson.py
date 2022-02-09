import json
import sys
from EntradaESaida.ArquivoDeMensagens import ArquivoDeMensagens

class EntradaESaidaDeMensagensJson(ArquivoDeMensagens):
    def importar(self, titulo_do_arquivo_com_mensagens: str):
        try:
            with open(titulo_do_arquivo_com_mensagens) as arquivo:
                dicionario_com_mensagens = json.load(arquivo)
                return dicionario_com_mensagens
        except:
            mensagem_de_erro = ("Erro ao importar arquivo com mensagens em" +
                    " formato JSON.")
            print(mensagem_de_erro, file=sys.stderr)
            return {}

    def exportar(self, mensagens, titulo_do_arquivo: str):
        try:
            with open(titulo_do_arquivo, "w") as arquivo:
                json.dump(mensagens, arquivo)
        except:
            mensagem_de_erro = ("Erro ao exportar arquivo com mensagens em" +
                    " formato JSON.")
            print(mensagem_de_erro, file=sys.stderr)

