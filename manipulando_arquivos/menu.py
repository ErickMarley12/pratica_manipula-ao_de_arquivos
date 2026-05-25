def menu():  
    print("1 - Cadastrar")
    print("2 - Ver cadastros")
    print("3 - Sair")
    opcao = input("Escolha uma opção:").strip()
    return opcao

def main():

    nomes = []

    while True:
        opcao = menu()
        if opcao == "1":
            nome = input("Digite o seu nome:").strip().title()
            nomes.append(nome)

            with open("cadastros.txt", "a") as arquivo:

                arquivo.write(nome + "\n")
        elif opcao == "2":
            with open("cadastros.txt", "r") as arquivo:
                print(arquivo.read())
     
            print(f"cadastrados: {nomes}")      
        elif opcao == "3":
            print("Saindo do programa...")
            break 
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()