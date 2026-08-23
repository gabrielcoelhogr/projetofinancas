from dataclasses import dataclass

@dataclass
class No:
    """Nó da árvore binária"""
    codigo: int      
    end: int     
    esquerda: 'No' = None
    direita: 'No' = None