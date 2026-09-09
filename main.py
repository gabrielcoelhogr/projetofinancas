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
                return banco.descricao
        return None

    def _buscar_pessoa_por_codigo(self, codigo):
        """Retorna o objeto Pessoa ou None"""
        for pessoa in self.pessoas:
            if pessoa.codigo == codigo:
                return pessoa.nome
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
            print(f"   ✓ {banco.nome}")
            
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
                print(f"  Banco: {banco.nome if banco else 'N/A'}")
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
                
                banco_nome = banco.nome if banco else "N/A"
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

    def menu(self):
        while True:
            print("=== GERENCIAR TRANSAÇÕES ===")
            print("1. Lançar Transação")
            print("2. Buscar")
            print("3. Listar")
            print("0. Voltar")
            
            opcao = input("Escolha: ")
            
            if opcao == "1":
                self.lançar()
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
        print("4. Gerenciar Contas")
        print("5. Gerenciar Transações")
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
        elif opcao == "4":  
            sistema = SistemaContas()
            sistema.menu()
        elif opcao == "5":  
            sistema = SistemaTransacoes()
            sistema.menu()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("✗ Opção inválida!\n")