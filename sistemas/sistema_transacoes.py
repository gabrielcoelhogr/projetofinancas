from models.transacao import Transacao
from models.categoria import Categoria
from models.conta_bancaria import ContaBancaria
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo

class SistemaTransacoes:
    """Gerencia a tabela de Transações com índice em árvore"""

    def __init__(self):
        self.arquivo = GerenciadorArquivo()
        self.arvore = ArvoreBinaria()
        self.transacoes = []
        
        # Carrega dados auxiliares
        self.categorias = []
        self.contas = []
        
        self.carregar()

    def carregar(self):
        print("Carregando transações...")
        
        # Carrega transações com índice
        self.transacoes, indices = self.arquivo.ler_com_indice("data/transacoes.txt", Transacao)
        for codigo, posicao in indices.items():
            self.arvore.inserir(codigo, posicao)
        
        # Carrega categorias e contas (sem índice, só pra lookup)
        self.categorias = self.arquivo.ler("data/categorias.txt", Categoria)
        self.contas = self.arquivo.ler("data/contas.txt", ContaBancaria)
        
        print(f"✓ {len(self.transacoes)} transações carregadas\n")

    def _buscar_categoria_por_codigo(self, codigo):
        """Retorna o objeto Categoria ou None"""
        for categoria in self.categorias:
            if categoria.codigo == codigo:
                return categoria
        return None

    def _buscar_conta_por_codigo(self, codigo):
        """Retorna o objeto ContaBancaria ou None"""
        for conta in self.contas:
            if conta.codigo == codigo:
                return conta
        return None

    def _buscar_posicao_conta_na_lista(self, codigo_conta):
        """Retorna a posição da conta na lista self.contas"""
        for i, conta in enumerate(self.contas):
            if conta.codigo == codigo_conta:
                return i
        return None

    def lançar(self):
        try:
            print("\n--- LANÇAR TRANSAÇÃO ---")
            codigo = int(input("Código: "))
            
            # Verificar se código já existe
            if self.arvore.buscar(codigo) is not None:
                print("✗ Erro: Esse código já existe!")
                return
            
            # Pedir código da categoria e verificar
            codigo_categoria = int(input("Código da Categoria: "))
            categoria = self._buscar_categoria_por_codigo(codigo_categoria)
            if categoria is None:
                print("✗ Erro: Categoria não encontrada!")
                return
            print(f"   ✓ {categoria.nome}")
            
            # Pedir código da conta e verificar
            codigo_conta = int(input("Código da Conta: "))
            conta = self._buscar_conta_por_codigo(codigo_conta)
            if conta is None:
                print("✗ Erro: Conta não encontrada!")
                return
            print(f"   ✓ Conta #{conta.codigo}")
            
            # Pedir data
            data = input("Data (YYYY-MM-DD): ")
            
            # Pedir valor
            valor = float(input("Valor: "))
            
            # Pedir débito/crédito
            print("\nTipo de operação:")
            print("D - Débito (saque)")
            print("C - Crédito (depósito)")
            debito_credito = input("Escolha (D/C): ").upper()
            
            if debito_credito not in ["D", "C"]:
                print("✗ Erro: Digite D ou C!")
                return
            
            # Criar objeto Transação
            transacao = Transacao(codigo, codigo_categoria, codigo_conta, data, valor, debito_credito)
            
            # ===== ATUALIZAR SALDO DA CONTA =====
            saldo_anterior = conta.saldo
            
            if debito_credito == "D":
                # Débito: SUBTRAI do saldo
                conta.saldo -= valor
                operacao = "Débito (Saque)"
            else:
                # Crédito: ADICIONA ao saldo
                conta.saldo += valor
                operacao = "Crédito (Depósito)"
            
            print(f"\n   Operação: {operacao}")
            print(f"   Saldo anterior: R$ {saldo_anterior:.2f}")
            print(f"   Saldo novo: R$ {conta.saldo:.2f}")
            
            # ===== GRAVAR TRANSAÇÃO =====
            
            # Adicionar transação à lista em memória
            self.transacoes.append(transacao)
            
            # Gravar transações em arquivo
            self.arquivo.gravar("data/transacoes.txt", self.transacoes, modo="w")
            
            # Inserir na árvore
            posicao = len(self.transacoes) - 1
            self.arvore.inserir(codigo, posicao)
            
            # ===== GRAVAR CONTA ATUALIZADA =====
            
            # Atualizar conta na lista self.contas
            posicao_conta = self._buscar_posicao_conta_na_lista(codigo_conta)
            if posicao_conta is not None:
                self.contas[posicao_conta] = conta
            
            # Gravar contas em arquivo
            self.arquivo.gravar("data/contas.txt", self.contas, modo="w")
            
            print("✓ Transação lançada com sucesso!\n")
        
        except ValueError:
            print("✗ Erro: Valores inválidos!\n")

    def buscar(self):
        try:
            print("\n--- BUSCAR TRANSAÇÃO ---")
            codigo = int(input("Código: "))
            
            no = self.arvore.buscar(codigo)
            
            if no is not None:
                posicao = no.end
                transacao = self.transacoes[posicao]
                
                # Buscar nomes associados
                categoria = self._buscar_categoria_por_codigo(transacao.codigo_categoria)
                conta = self._buscar_conta_por_codigo(transacao.codigo_conta)
                
                tipo = "Débito (Saque)" if transacao.debito_credito == "D" else "Crédito (Depósito)"
                
                print(f"\n✓ Código: {transacao.codigo}")
                print(f"  Categoria: {categoria.nome if categoria else 'N/A'}")
                print(f"  Conta: #{conta.codigo if conta else 'N/A'}")
                print(f"  Data: {transacao.data}")
                print(f"  Valor: R$ {transacao.valor:.2f}")
                print(f"  Tipo: {tipo}\n")
            else:
                print("✗ Transação não encontrada!\n")
        
        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def listar(self):
        if not self.transacoes:
            print("\n✗ Nenhuma transação cadastrada!\n")
        else:
            print("\n--- TRANSAÇÕES CADASTRADAS ---")
            for i, transacao in enumerate(self.transacoes, 1):
                categoria = self._buscar_categoria_por_codigo(transacao.codigo_categoria)
                tipo = "D" if transacao.debito_credito == "D" else "C"
                
                categoria_nome = categoria.nome if categoria else "N/A"
                
                print(f"{i}. [{transacao.codigo}] {transacao.data} | {categoria_nome} | R$ {transacao.valor:.2f} ({tipo})")
            print()

    def excluir(self):
        try:
            print("\n--- EXCLUIR TRANSAÇÃO ---")
            codigo = int(input("Código: "))

            # Buscar transação
            transacao_encontrada = None
            posicao_transacao = -1

            for i, transacao in enumerate(self.transacoes):
                if transacao.codigo == codigo:
                    transacao_encontrada = transacao
                    posicao_transacao = i
                    break

            if transacao_encontrada is None:
                print("✗ Transação não encontrada!\n")
                return

            # Mostrar dados
            categoria = self._buscar_categoria_por_codigo(transacao_encontrada.codigo_categoria)
            conta = self._buscar_conta_por_codigo(transacao_encontrada.codigo_conta)

            tipo = "Débito (Saque)" if transacao_encontrada.debito_credito == "D" else "Crédito (Depósito)"

            print(f"\n✓ Transação encontrada:")
            print(f"  Categoria: {categoria.nome if categoria else 'N/A'}")
            print(f"  Conta: #{conta.codigo if conta else 'N/A'}")
            print(f"  Data: {transacao_encontrada.data}")
            print(f"  Valor: R$ {transacao_encontrada.valor:.2f}")
            print(f"  Tipo: {tipo}")

            # Confirmar exclusão
            confirmacao = input("\nDeseja realmente excluir? (S/N): ").upper()

            if confirmacao != "S":
                print("✗ Exclusão cancelada!\n")
                return

            # ===== REVERTER SALDO =====
            if conta:
                posicao_conta = self._buscar_posicao_conta_na_lista(conta.codigo)

                if transacao_encontrada.debito_credito == "D":
                    conta.saldo += transacao_encontrada.valor
                else:
                    conta.saldo -= transacao_encontrada.valor

                if posicao_conta is not None:
                    self.contas[posicao_conta] = conta

            # ===== REMOVER TRANSAÇÃO =====
            self.transacoes.pop(posicao_transacao)

            # Rebuild da árvore para manter o índice consistente
            self.arvore = ArvoreBinaria()
            for indice, transacao in enumerate(self.transacoes):
                self.arvore.inserir(transacao.codigo, indice)

            # Gravar arquivo de transações
            self.arquivo.gravar("data/transacoes.txt", self.transacoes, modo="w")

            # Gravar arquivo de contas
            self.arquivo.gravar("data/contas.txt", self.contas, modo="w")

            print("✓ Transação excluída com sucesso!\n")

        except ValueError:
            print("✗ Erro: Código deve ser um número!\n")

    def menu(self):
        while True:
            print("=== GERENCIAR TRANSAÇÕES ===")
            print("1. Lançar Transação")
            print("2. Buscar")
            print("3. Listar")
            print("4. Excluir")
            print("0. Voltar")

            opcao = input("Escolha: ")

            if opcao == "1":
                self.lançar()
            elif opcao == "2":
                self.buscar()
            elif opcao == "3":
                self.listar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "0":
                break
            else:
                print("✗ Opção inválida!\n")