from models.conta_bancaria import ContaBancaria
from models.categoria import Categoria
from models.transacao import Transacao
from models.banco import Banco
from models.pessoa import Pessoa
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

class SistemaRelatorios:
    """Gerencia relatórios do sistema de finanças"""

    def __init__(self):
        self.arquivo = GerenciadorArquivo()
        
        # Carrega dados
        self.transacoes = []
        self.contas = []
        self.categorias = []
        self.bancos = []
        self.pessoas = []
        
        self.carregar()

    def carregar(self):
        print("Carregando dados para relatórios...")
        
        # Lê transações
        self.transacoes = self.arquivo.ler("data/transacoes.txt", Transacao)
        
        # Lê contas
        self.contas = self.arquivo.ler("data/contas.txt", ContaBancaria)
        
        # Lê categorias
        self.categorias = self.arquivo.ler("data/categorias.txt", Categoria)
        
        # Lê bancos
        self.bancos = self.arquivo.ler("data/bancos.txt", Banco)
        
        # Lê pessoas
        self.pessoas = self.arquivo.ler("data/pessoas.txt", Pessoa)
        
        print(f"✓ Dados carregados\n")

    def _buscar_categoria_por_codigo(self, codigo):
        """Retorna o nome da categoria ou None"""
        for categoria in self.categorias:
            if categoria.codigo == codigo:
                return categoria.nome
        return "N/A"

    def _buscar_banco_por_codigo(self, codigo):
        """Retorna o nome do banco ou None"""
        for banco in self.bancos:
            if banco.codigo == codigo:
                return banco.descricao
        return "N/A"

    def _buscar_pessoa_por_codigo(self, codigo):
        """Retorna o nome da pessoa ou None"""
        for pessoa in self.pessoas:
            if pessoa.codigo == codigo:
                return pessoa.nome
        return "N/A"

    def _buscar_conta_por_codigo(self, codigo):
        """Retorna o objeto ContaBancaria ou None"""
        for conta in self.contas:
            if conta.codigo == codigo:
                return conta
        return None

    def relatorio_por_periodo(self):
        try:
            print("\n--- RELATÓRIO DE TRANSAÇÕES POR PERÍODO ---")
            
            data_inicial = input("Data inicial (YYYY-MM-DD): ")
            data_final = input("Data final (YYYY-MM-DD): ")
            
            # Filtrar transações no período
            transacoes_periodo = []
            for transacao in self.transacoes:
                if data_inicial <= transacao.data <= data_final:
                    transacoes_periodo.append(transacao)
            
            if not transacoes_periodo:
                print("\n✗ Nenhuma transação neste período!\n")
                return
            
            # Calcular somas
            soma_debitos = 0.0
            soma_creditos = 0.0
            
            for transacao in transacoes_periodo:
                if transacao.debito_credito == "D":
                    soma_debitos += transacao.valor
                else:
                    soma_creditos += transacao.valor
            
            saldo_periodo = soma_creditos - soma_debitos
            
            # Mostrar relatório
            print(f"\n=== TRANSAÇÕES DE {data_inicial} ATÉ {data_final} ===\n")
            
            for i, trans in enumerate(transacoes_periodo, 1):
                categoria = self._buscar_categoria_por_codigo(trans.codigo_categoria)
                tipo = "D" if trans.debito_credito == "D" else "C"
                
                print(f"{i}. [{trans.codigo}] {trans.data} | {categoria} | R$ {trans.valor:.2f} ({tipo})")
            
            print(f"\n--- RESUMO DO PERÍODO ---")
            print(f"Total de Débitos:  R$ {soma_debitos:.2f}")
            print(f"Total de Créditos: R$ {soma_creditos:.2f}")
            print(f"Saldo do Período:  R$ {saldo_periodo:.2f}\n")
        
        except ValueError:
            print("✗ Erro: Data inválida!\n")

    def saldos_contas(self):
        if not self.contas:
            print("\n✗ Nenhuma conta cadastrada!\n")
            return
        
        print("\n--- SALDOS DE TODAS AS CONTAS ---\n")
        
        saldo_total = 0.0
        
        for i, conta in enumerate(self.contas, 1):
            # Buscar banco e pessoa
            banco = self._buscar_banco_por_codigo(conta.codigo_banco)
            pessoa = self._buscar_pessoa_por_codigo(conta.codigo_pessoa)
            
            print(f"{i}. Conta #{conta.codigo}")
            print(f"   Banco: {banco}")
            print(f"   Pessoa: {pessoa}")
            print(f"   Descrição: {conta.descricao}")
            print(f"   Saldo: R$ {conta.saldo:.2f}\n")
            
            saldo_total += conta.saldo
        
        print(f"--- SALDO TOTAL DE TODAS AS CONTAS ---")
        print(f"R$ {saldo_total:.2f}\n")

    def saldo_geral(self):
        print("\n--- SALDO GERAL DO SISTEMA ---\n")
        
        if not self.contas:
            print("Nenhuma conta cadastrada!")
            print("Saldo Geral: R$ 0.00\n")
            return
        
        saldo_total = 0.0
        
        for conta in self.contas:
            saldo_total += conta.saldo
        
        print(f"Você tem {len(self.contas)} conta(s) no sistema")
        print(f"Saldo Geral: R$ {saldo_total:.2f}\n")

    def menu(self):
        while True:
            print("=== RELATÓRIOS ===")
            print("1. Transações por Período")
            print("2. Saldos de Todas as Contas")
            print("3. Saldo Geral do Sistema")
            print("0. Voltar")
            
            opcao = input("Escolha: ")
            
            if opcao == "1":
                self.relatorio_por_periodo()
            elif opcao == "2":
                self.saldos_contas()
            elif opcao == "3":
                self.saldo_geral()
            elif opcao == "0":
                break
            else:
                print("✗ Opção inválida!\n")