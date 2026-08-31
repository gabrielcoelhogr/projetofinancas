from models.banco import Banco
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

print("=== TESTE DO SISTEMA DE BANCOS ===\n")

# Criar instância do gerenciador
g = GerenciadorArquivo()
arvore = ArvoreBinaria()

# ===== TESTE 1: Gravar bancos =====
print("1. Gravando 3 bancos...")
b1 = Banco(1, "Banco do Brasil")
b2 = Banco(2, "Caixa Econômica")
b3 = Banco(3, "Itaú")

g.gravar("data/bancos.txt", [b1, b2, b3], modo="w")
print("✓ Gravado em data/bancos.txt\n")

# ===== TESTE 2: Ler bancos =====
print("2. Lendo bancos...")
bancos = g.ler("data/bancos.txt", Banco)
for b in bancos:
    print(f"   {b}")
print()

# ===== TESTE 3: Ler com índice (pra árvore) =====
print("3. Lendo com índice (pra árvore)...")
bancos, indices = g.ler_com_indice("data/bancos.txt", Banco)
print(f"   Bancos: {bancos}")
print(f"   Índices: {indices}")
print()

# ===== TESTE 4: Testar busca na árvore =====
print("4. Testando busca na árvore...")
for codigo, posicao in indices.items():
    arvore.inserir(codigo, posicao)

no = arvore.buscar(2)
if no:
    banco = bancos[no.end]
    print(f"   ✓ Encontrado (código 2): {banco}")
else:
    print("   ✗ Não encontrado!")
print()

# ===== TESTE 5: Adicionar um banco novo =====
print("5. Adicionando um novo banco...")
b4 = Banco(4, "Santander")
g.gravar("data/bancos.txt", b4, modo="a")
print("✓ Adicionado!\n")

# ===== TESTE 6: Ler de novo (com o novo) =====
print("6. Lendo de novo...")
bancos = g.ler("data/bancos.txt", Banco)
for b in bancos:
    print(f"   {b}")

print("\n✅ TODOS OS TESTES PASSARAM!")