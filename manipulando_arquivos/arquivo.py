def cadastrar(nome):
    with open("cadastros.txt", "a") as arquivo:
        arquivo.write(nome + "\n")

def listar():
    try:
        with open("cadastros.txt", "r") as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "Nenhum cadastro encontrado."