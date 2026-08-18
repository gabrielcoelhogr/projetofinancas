from dataclasses import dataclass

@dataclass
class ContaBancaria:
    codigo : int
    codigo_banco : int
    codigo_pessoa : int
    descricao : str
    saldo : float