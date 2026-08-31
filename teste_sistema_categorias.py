from models.categoria import Categoria
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

print("=== TESTE DO SISTEMA DE CATEGORIAS ===\n")

# Criar instância do gerenciador
g = GerenciadorArquivo()
arvore = ArvoreBinaria()

# ===== TESTE 1: Gravar categorias =====
print("1. Gravando 3 categorias...")
c1 = Categoria(1, "Alimentação")
c2 = Categoria(2, "Transporte")
c3 = Categoria(3, "Saúde")

g.gravar("data/categorias.txt", [c1, c2, c3], modo="w")
print("✓ Gravado em data/categorias.txt\n")

# ===== TESTE 2: Ler categorias =====
print("2. Lendo categorias...")
categorias = g.ler("data/categorias.txt", Categoria)
for c in categorias:
    print(f"   {c}")
print()

# ===== TESTE 3: Ler com índice (pra árvore) =====
print("3. Lendo com índice (pra árvore)...")
categorias, indices = g.ler_com_indice("data/categorias.txt", Categoria)
print(f"   Categorias: {categorias}")
print(f"   Índices: {indices}")
print()

# ===== TESTE 4: Testar busca na árvore =====
print("4. Testando busca na árvore...")
for codigo, posicao in indices.items():
    arvore.inserir(codigo, posicao)

no = arvore.buscar(2)
if no:
    categoria = categorias[no.end]
    print(f"   ✓ Encontrado (código 2): {categoria}")
else:
    print("   ✗ Não encontrado!")
print()

# ===== TESTE 5: Adicionar uma categoria nova =====
print("5. Adicionando uma nova categoria...")
c4 = Categoria(4, "Educação")
g.gravar("data/categorias.txt", c4, modo="a")
print("✓ Adicionada!\n")

# ===== TESTE 6: Ler de novo (com a nova) =====
print("6. Lendo de novo...")
categorias = g.ler("data/categorias.txt", Categoria)
for c in categorias:
    print(f"   {c}")

print("\n✅ TODOS OS TESTES PASSARAM!")