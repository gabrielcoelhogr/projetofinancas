from models.categoria import Categoria
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

class SistemaCategorias:
    """Gerencia a tabela de Categorias com índice em árvore"""

    def __init__(self):
        self.arquivo = GerenciadorArquivo()
        self.arvore = ArvoreBinaria()
        self.categorias = []
        self.carregar()

    def carregar(self):
        print("Carregando categorias...")
        self.categorias, indices = self.arquivo.ler_com_indice("data/categorias.txt", Categoria)
        for codigo, posicao in indices.items():
            self.arvore.inserir(codigo, posicao)
        print(f"✓ {len(self.categorias)} categorias carregadas\n")

    def incluir(self):
        try:
            print("\n--- INCLUIR CATEGORIA ---")
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            
            if self.arvore.buscar(codigo) is not None:
                print("✗ Erro: Esse código já existe!")
                return
            
            categoria = Categoria(codigo, nome)
            self.categorias.append(categoria)
            self.arquivo.gravar("data/categorias.txt", self.categorias, modo="w")
            posicao = len(self.categorias) - 1
            self.arvore.inserir(codigo, posicao)
            print("✓ Categoria adicionada com sucesso!\n")
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def buscar(self):
        try:
            print("\n--- BUSCAR CATEGORIA ---")
            codigo = int(input("Código: "))
            no = self.arvore.buscar(codigo)
            
            if no is not None:
                posicao = no.end
                categoria = self.categorias[posicao]
                print(f"\n✓ {categoria}\n")
            else:
                print("✗ Categoria não encontrada!\n")
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def listar(self):
        if not self.categorias:
            print("\n✗ Nenhuma categoria cadastrada!\n")
        else:
            print("\n--- CATEGORIAS CADASTRADAS ---")
            for i, categoria in enumerate(self.categorias, 1):
                print(f"{i}. {categoria}")
            print()

    def menu(self):
        while True:
            print("=== GERENCIAR CATEGORIAS ===")
            print("1. Incluir")
            print("2. Buscar")
            print("3. Listar")
            print("0. Voltar")
            
            opcao = input("Escolha: ")
            
            if opcao == "1":
                self.incluir()
            elif opcao == "2":
                self.buscar()
            elif opcao == "3":
                self.listar()
            elif opcao == "0":
                break
            else:
                print("✗ Opção inválida!\n")