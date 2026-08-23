"""Tem que trocar na busac para end para testar dnv"""
from index.arvore_binaria import ArvoreBinaria

arvore = ArvoreBinaria()

arvore.inserir(5, 0)
arvore.inserir(3, 1)
arvore.inserir(7, 2)
arvore.inserir(1, 3)
arvore.inserir(9, 4)

print("✓ Árvore criada com 5 nós")

print(f"\nBuscar código 5: posição {arvore.buscar(5)}")  # 0
print(f"Buscar código 3: posição {arvore.buscar(3)}")  # 1
print(f"Buscar código 7: posição {arvore.buscar(7)}")  # 2
print(f"Buscar código 1: posição {arvore.buscar(1)}")  # 3
print(f"Buscar código 9: posição {arvore.buscar(9)}")  # 4
print(f"Buscar código 99: posição {arvore.buscar(99)}")  # None