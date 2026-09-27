from models.pessoa import Pessoa
from models.categoria import Categoria
from models.conta_bancaria import ContaBancaria
from models.banco import Banco
from models.transacao import Transacao
from index.arvore_binaria import ArvoreBinaria
from utils.arquivo import GerenciadorArquivo
from sistemas.sistema_pessoas import SistemaPessoas
from sistemas.sistema_categorias import SistemaCategorias
from sistemas.sistema_bancos import SistemaBancos
from sistemas.sistema_contas import SistemaContas
from sistemas.sistema_transacoes import SistemaTransacoes
from sistemas.sistema_relatorios import SistemaRelatorios

if __name__ == "__main__":
    # Menu Principal
    while True:
        print("\n=== SISTEMA DE FINANÇAS PESSOAIS ===")
        print("1. Gerenciar Pessoas")
        print("2. Gerenciar Categorias")
        print("3. Gerenciar Bancos")
        print("4. Gerenciar Contas")
        print("5. Gerenciar Transações")
        print("6. Relatórios")
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
        elif opcao == "6":
            sistema = SistemaRelatorios()
            sistema.menu()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("✗ Opção inválida!\n")