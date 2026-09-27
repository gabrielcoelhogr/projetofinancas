from models.banco import Banco
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

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