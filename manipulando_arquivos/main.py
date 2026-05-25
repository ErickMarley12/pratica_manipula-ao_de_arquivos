from menu import menu
from arquivo import cadastrar, listar


##FORMA DE ORGANIZAR O CÓDIGO MELHOR. CONSIGO DIVIDIR EM ARQUIVO,INTERFACE,MENU E MAIN. mamão com açucar 

def main():
    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Digite o seu nome: ").strip().title()
            cadastrar(nome)

        elif opcao == "2":
            print("\nCADASTROS:")
            print(listar())
        elif opcao == "3":
            print("Finalizando o programa...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__": #até agora n entendi direito. mas faz o código executar oq eu quero :0

    main() 