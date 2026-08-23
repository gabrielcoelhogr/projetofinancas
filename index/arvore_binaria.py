from .no import No

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, codigo, posicao):
        """Insere um novo nó na árvore"""
        novo = No(codigo, posicao)

        # se árvore estiver sem nada o novo nó vira a raiz
        if self.raiz is None:
            self.raiz = novo
            return

        pai = None
        atual = self.raiz

        while atual is not None:
            pai = atual
            if codigo < atual.codigo:
                atual = atual.esquerda
            else:
                atual = atual.direita

        #se o novo nó é filho esquerdo ou direito do pai
        if codigo < pai.codigo:
            pai.esquerda = novo
        else:
            pai.direita = novo

    def buscar(self, codigo):
        """Busca um nó pelo código. Retorna o nó ou Nulo."""
        atual = self.raiz

        while atual is not None:
            if codigo == atual.codigo:
                return atual
            elif codigo < atual.codigo:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return None  # não encontrou