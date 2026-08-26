from main import SistemaPessoas

# Iniciar o sistema (vai carregar pessoas.txt se existir)
sistema = SistemaPessoas()

# Testar incluir
print("=== TESTE DE INCLUSÃO ===")
# Simular input do usuário (precisa fazer manual ou usar input())
# Por enquanto, adiciona direto:

from models.pessoa import Pessoa
p1 = Pessoa(1, "João Silva")
p2 = Pessoa(2, "Maria Santos")

sistema.pessoas = [p1, p2]
sistema.arquivo.gravar("data/pessoas.txt", sistema.pessoas, modo="w")
sistema.arvore.inserir(1, 0)
sistema.arvore.inserir(2, 1)

print("✓ 2 pessoas adicionadas\n")

# Testar busca
print("=== TESTE DE BUSCA ===")
no = sistema.arvore.buscar(1)
if no:
    pessoa = sistema.pessoas[no.end]
    print(f"✓ Encontrado: {pessoa}\n")

# Testar listagem
print("=== TESTE DE LISTAGEM ===")
sistema.listar()

print("✅ TESTES CONCLUÍDOS!")