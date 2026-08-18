from dataclasses import dataclass

@dataclass
class Transacao:
    codigo : int 
    codigo_categoria : int
    codigo_conta : int
    data : str
    valor : float
    debito_credito : str
    