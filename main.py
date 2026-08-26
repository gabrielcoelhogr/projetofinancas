from models.pessoa import Pessoa
from models.categoria import Categoria
from models.conta_bancaria import ContaBancaria
from models.banco import Banco
from models.transacao import Transacao
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

class SistemaPessoas:
    #Gerencia as pessoas

    def __init__(self):
        self.arquivo = GerenciadorArquivo()
        self.arvore = ArvoreBinaria()
        self.pessoa = []

        #Carrega arquivos ao iniciar
        self.carregar()

    def carregar(self):
        #Carrega pessoas do arquivo e reconstrói a árvore binária chamando ao iniciar o programa
        
        print("Carregando pessoas...")
        
        #Ler arquivo com índices
        self.pessoas, indices = self.arquivo.ler_com_indice("dados/pessoas.txt", Pessoa)
        
        #Reconstruir árvore
        for codigo, posicao in indices.items():
            self.arvore.inserir(codigo, posicao)
        
        print(f"✓ {len(self.pessoas)} pessoas carregadas\n")

    def incluir(self):

        try:
            print("\n--- INCLUIR PESSOA ---")
            codigo = int(input("Código: "))
            nome = input("Nome: ")
            
            # Verificar se código já existe
            if self.arvore.buscar(codigo) is not None:
                print("✗ Erro: Esse código já existe!")
                return
            
            # Criar objeto
            pessoa = Pessoa(codigo, nome)
            
            # Adicionar à lista em memória
            self.pessoas.append(pessoa)
            
            # Gravar em arquivo (reescreve tudo)
            self.arquivo.gravar("dados/pessoas.txt", self.pessoas, modo="w")
            
            # Inserir na árvore (posição = última linha)
            posicao = len(self.pessoas) - 1
            no = self.arvore.inserir(codigo, posicao)
            
            print("✓ Pessoa adicionada com sucesso!\n")
        
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def buscar(self):
        
        try:
            print("\n--- BUSCAR PESSOA ---")
            codigo = int(input("Código: "))
            
            # Buscar na árvore (retorna o Nó)
            no = self.arvore.buscar(codigo)
            
            if no is not None:
                # Usar a posição pra acessar a pessoa na lista
                posicao = no.end
                pessoa = self.pessoas[posicao]
                print(f"\n✓ {pessoa}\n")
            else:
                print("✗ Pessoa não encontrada!\n")
        
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def listar(self):
        #Lista todas as pessoas em ordem de inclusão"""
        if not self.pessoas:
            print("\n✗ Nenhuma pessoa cadastrada!\n")
        else:
            print("\n--- PESSOAS CADASTRADAS ---")
            for i, pessoa in enumerate(self.pessoas, 1):
                print(f"{i}. {pessoa}")
            print()

    def menu(self):
        # Menu de Pessoas
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

if __name__ == "__main__":
    sistema = SistemaPessoas()
    sistema.menu()