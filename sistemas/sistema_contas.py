from models.conta_bancaria import ContaBancaria
from models.banco import Banco
from models.pessoa import Pessoa
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

class SistemaContas:
    """Gerencia a tabela de Contas Bancárias com índice em árvore"""

    def __init__(self):
        self.arquivo = GerenciadorArquivo()
        self.arvore = ArvoreBinaria()
        self.contas = []
        
        # Carrega também Bancos e Pessoas pra buscar nomes
        self.bancos = []
        self.pessoas = []
        
        self.carregar()

    def carregar(self):
        print("Carregando contas bancárias...")
        
        # Carrega contas com índice
        self.contas, indices = self.arquivo.ler_com_indice("data/contas.txt", ContaBancaria)
        for codigo, posicao in indices.items():
            self.arvore.inserir(codigo, posicao)
        
        # Carrega bancos e pessoas (sem índice, só pra lookup)
        self.bancos = self.arquivo.ler("data/bancos.txt", Banco)
        self.pessoas = self.arquivo.ler("data/pessoas.txt", Pessoa)
        
        print(f"✓ {len(self.contas)} contas carregadas\n")

    def _buscar_banco_por_codigo(self, codigo):
        """Retorna o objeto Banco ou None"""
        for banco in self.bancos:
            if banco.codigo == codigo:
                return banco
        return None

    def _buscar_pessoa_por_codigo(self, codigo):
        """Retorna o objeto Pessoa ou None"""
        for pessoa in self.pessoas:
            if pessoa.codigo == codigo:
                return pessoa
        return None

    def incluir(self):
        try:
            print("\n--- INCLUIR CONTA ---")
            codigo = int(input("Código: "))
            
            # Verificar se código já existe
            if self.arvore.buscar(codigo) is not None:
                print("✗ Erro: Esse código já existe!")
                return
            
            # Pedir código do banco e verificar
            codigo_banco = int(input("Código do Banco: "))
            banco = self._buscar_banco_por_codigo(codigo_banco)
            if banco is None:
                print("✗ Erro: Banco não encontrado!")
                return
            print(f"   ✓ {banco.descricao}")
            
            # Pedir código da pessoa e verificar
            codigo_pessoa = int(input("Código da Pessoa: "))
            pessoa = self._buscar_pessoa_por_codigo(codigo_pessoa)
            if pessoa is None:
                print("✗ Erro: Pessoa não encontrada!")
                return
            print(f"   ✓ {pessoa.nome}")
            
            # Pedir outros dados
            descricao = input("Descrição: ")
            saldo = float(input("Saldo: "))
            
            # Criar objeto
            conta = ContaBancaria(codigo, codigo_banco, codigo_pessoa, descricao, saldo)
            
            # Adicionar à lista em memória
            self.contas.append(conta)
            
            # Gravar em arquivo
            self.arquivo.gravar("data/contas.txt", self.contas, modo="w")
            
            # Inserir na árvore
            posicao = len(self.contas) - 1
            self.arvore.inserir(codigo, posicao)
            
            print("✓ Conta adicionada com sucesso!\n")
        
        except ValueError:
            print("✗ Erro: Valores inválidos!\n")

    def buscar(self):
        try:
            print("\n--- BUSCAR CONTA ---")
            codigo = int(input("Código: "))
            
            no = self.arvore.buscar(codigo)
            
            if no is not None:
                posicao = no.end
                conta = self.contas[posicao]
                
                # Buscar nomes associados
                banco = self._buscar_banco_por_codigo(conta.codigo_banco)
                pessoa = self._buscar_pessoa_por_codigo(conta.codigo_pessoa)
                
                print(f"\n✓ Código: {conta.codigo}")
                print(f"  Banco: {banco.descricao if banco else 'N/A'}")
                print(f"  Pessoa: {pessoa.nome if pessoa else 'N/A'}")
                print(f"  Descrição: {conta.descricao}")
                print(f"  Saldo: R$ {conta.saldo:.2f}\n")
            else:
                print("✗ Conta não encontrada!\n")
        
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def listar(self):
        if not self.contas:
            print("\n✗ Nenhuma conta cadastrada!\n")
        else:
            print("\n--- CONTAS CADASTRADAS ---")
            for i, conta in enumerate(self.contas, 1):
                banco = self._buscar_banco_por_codigo(conta.codigo_banco)
                pessoa = self._buscar_pessoa_por_codigo(conta.codigo_pessoa)
                
                banco_nome = banco.descricao if banco else "N/A"
                pessoa_nome = pessoa.nome if pessoa else "N/A"
                
                print(f"{i}. [{conta.codigo}] {banco_nome} - {pessoa_nome} - R$ {conta.saldo:.2f}")
            print()

    def menu(self):
        while True:
            print("=== GERENCIAR CONTAS ===")
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