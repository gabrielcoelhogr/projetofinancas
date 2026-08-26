import json
from dataclasses import asdict

class GerenciadorArquivo:
    #Gerencia leitura e escrita de arquivos JSON#
    
    @staticmethod
    def gravar(caminho, objetos, modo="w"):
        #Grava lista de objetos em arquivo JSON (uma pessoa por linha)#

        if not isinstance(objetos, list):
            objetos = [objetos]
        
        with open(caminho, modo) as f:
            for obj in objetos:
                d = asdict(obj)
                f.write(json.dumps(d) + "\n")

    @staticmethod
    def ler(caminho, classe):
        #Lê arquivo JSON e reconstrói objetos da classe
        
        objetos = []
        try:
            with open(caminho, "r") as f:
                for linha in f:
                    d = json.loads(linha)
                    obj = classe(**d)
                    objetos.append(obj)
        except FileNotFoundError:
            pass  # Arquivo não existe ainda, retorna lista vazia
        
        return objetos

    @staticmethod
    def ler_com_indice(caminho, classe):
        #Lê arquivo JSON e retorna objetos + dicionário de índices 
        #Usada pra reconstruir a árvore binária ao iniciar o programa
        
        objetos = []
        indices = {}
        
        try:
            with open(caminho, "r") as f:
                for i, linha in enumerate(f):
                    d = json.loads(linha)
                    obj = classe(**d)
                    objetos.append(obj)
                    indices[obj.codigo] = i  # Guarda a linha onde está
        except FileNotFoundError:
            pass
        
        return objetos, indices