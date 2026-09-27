from models.pessoa import Pessoa
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