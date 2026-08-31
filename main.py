from models.pessoa import Pessoa
from models.categoria import Categoria
from models.conta_bancaria import ContaBancaria
from models.banco import Banco
from models.transacao import Transacao
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

class SistemaPessoas:
    """Gerencia a tabela de Pessoas com índice em árvore"""

    def __init__(self):
        self.arquivo = GerenciadorArquivo()
        self.arvore = ArvoreBinaria()
        self.pessoas = []
        self.carregar()

    def carregar(self):
        print("Carregando pessoas...")
        self.pessoas, indices = self.arquivo.ler_com_indice("data/pessoas.txt", Pessoa)
        for codigo, posicao in indices.items():
            self.arvore.inserir(codigo, posicao)
        print(f"✓ {len(self.pessoas)} pessoas carregadas\n")

    def incluir(self):
        try:
            print("\n--- INCLUIR PESSOA ---")
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            
            if self.arvore.buscar(codigo) is not None:
                print("✗ Erro: Esse código já existe!")
                return
            
            pessoa = Pessoa(codigo, nome)
            self.pessoas.append(pessoa)
            self.arquivo.gravar("data/pessoas.txt", self.pessoas, modo="w")
            posicao = len(self.pessoas) - 1
            self.arvore.inserir(codigo, posicao)
            print("✓ Pessoa adicionada com sucesso!\n")
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def buscar(self):
        try:
            print("\n--- BUSCAR PESSOA ---")
            codigo = int(input("Código: "))
            no = self.arvore.buscar(codigo)
            
            if no is not None:
                posicao = no.end
                pessoa = self.pessoas[posicao]
                print(f"\n✓ {pessoa}\n")
            else:
                print("✗ Pessoa não encontrada!\n")
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def listar(self):
        if not self.pessoas:
            print("\n✗ Nenhuma pessoa cadastrada!\n")
        else:
            print("\n--- PESSOAS CADASTRADAS ---")
            for i, pessoa in enumerate(self.pessoas, 1):
                print(f"{i}. {pessoa}")
            print()

    def menu(self):
        while True:
            print("=== GERENCIAR PESSOAS ===")
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


class SistemaBancos:
    """Gerencia a tabela de Bancos com índice em árvore"""

    def __init__(self):
        self.arquivo = GerenciadorArquivo()
        self.arvore = ArvoreBinaria()
        self.bancos = []
        self.carregar()

    def carregar(self):
        print("Carregando bancos...")
        self.bancos, indices = self.arquivo.ler_com_indice("data/bancos.txt", Banco)
        for codigo, posicao in indices.items():
            self.arvore.inserir(codigo, posicao)
        print(f"✓ {len(self.bancos)} bancos carregados\n")

    def incluir(self):
        try:
            print("\n--- INCLUIR BANCO ---")
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            
            if self.arvore.buscar(codigo) is not None:
                print("✗ Erro: Esse código já existe!")
                return
            
            banco = Banco(codigo, nome)
            self.bancos.append(banco)
            self.arquivo.gravar("data/bancos.txt", self.bancos, modo="w")
            posicao = len(self.bancos) - 1
            self.arvore.inserir(codigo, posicao)
            print("✓ Banco adicionado com sucesso!\n")
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def buscar(self):
        try:
            print("\n--- BUSCAR BANCO ---")
            codigo = int(input("Código: "))
            no = self.arvore.buscar(codigo)
            
            if no is not None:
                posicao = no.end
                banco = self.bancos[posicao]
                print(f"\n✓ {banco}\n")
            else:
                print("✗ Banco não encontrado!\n")
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def listar(self):
        if not self.bancos:
            print("\n✗ Nenhum banco cadastrado!\n")
        else:
            print("\n--- BANCOS CADASTRADOS ---")
            for i, banco in enumerate(self.bancos, 1):
                print(f"{i}. {banco}")
            print()

    def menu(self):
        while True:
            print("=== GERENCIAR BANCOS ===")
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


if __name__ == "__main__":
    # Menu Principal
    while True:
        print("\n=== SISTEMA DE FINANÇAS PESSOAIS ===")
        print("1. Gerenciar Pessoas")
        print("2. Gerenciar Categorias")
        print("3. Gerenciar Bancos")
        print("0. Sair")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            sistema = SistemaPessoas()
            sistema.menu()
        elif opcao == "2":
            sistema = SistemaCategorias()
            sistema.menu()
        elif opcao == "3":
            sistema = SistemaBancos()
            sistema.menu()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("✗ Opção inválida!\n")