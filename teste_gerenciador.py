from models.pessoa import Pessoa
from models.categoria import Categoria
from utils.arquivo import GerenciadorArquivo

print("=== TESTE DO GERENCIADOR DE ARQUIVO ===\n")

# Criar instância do gerenciador
g = GerenciadorArquivo()

# ===== TESTE 1: Gravar pessoas =====
print("1. Gravando 3 pessoas...")
p1 = Pessoa(1, "João")
p2 = Pessoa(2, "Maria")
p3 = Pessoa(3, "Pedro")

g.gravar("data/pessoas.txt", [p1, p2, p3], modo="w")
print("✓ Gravado em data/pessoas.txt\n")

# ===== TESTE 2: Ler pessoas =====
print("2. Lendo pessoas...")
pessoas = g.ler("data/pessoas.txt", Pessoa)
for p in pessoas:
    print(f"   {p}")
print()

# ===== TESTE 3: Ler com índice (pra árvore) =====
print("3. Lendo com índice (pra árvore)...")
pessoas, indices = g.ler_com_indice("data/pessoas.txt", Pessoa)
print(f"   Pessoas: {pessoas}")
print(f"   Índices: {indices}")
print()

# ===== TESTE 4: Adicionar uma pessoa nova =====
print("4. Adicionando uma nova pessoa...")
p4 = Pessoa(4, "Ana")
g.gravar("data/pessoas.txt", p4, modo="a")
print("✓ Adicionada!\n")

# ===== TESTE 5: Ler de novo (com a nova) =====
print("5. Lendo de novo...")
pessoas = g.ler("data/pessoas.txt", Pessoa)
for p in pessoas:
    print(f"   {p}")
print()

# ===== TESTE 6: Gravar categorias =====
print("6. Gravando categorias...")
c1 = Categoria(1, "Alimentação")
c2 = Categoria(2, "Transporte")

g.gravar("data/categorias.txt", [c1, c2])
print("✓ Gravado!\n")

# ===== TESTE 7: Ler categorias =====
print("7. Lendo categorias...")
categorias = g.ler("dados/categorias.txt", Categoria)
for c in categorias:
    print(f"   {c}")

print("\n✅ TODOS OS TESTES PASSARAM!")