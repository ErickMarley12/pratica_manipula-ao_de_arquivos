import tkinter as tk
from arquivo import cadastrar, listar

def salvar_nome():
    nome = entrada.get().strip().title()

    if nome == "":
        resultado.config(text="Por favor, digite um nome.")
        return
    
    cadastrar(nome)
    entrada.delete(0, tk.END)
    resultado.config(text=f"nome '{nome})' cadastrado com sucesso!")


def mostrar_cadastros():
    dados = listar()
    resultado.config(text=dados)

 #janela principal  seja oq deus quiser, o que importa é que funcione
janela = tk.Tk()
janela.title("Cadastro de Nomes")
janela.geometry("400x300")

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

botao_cadastrar = tk.Button(
    janela,
    text="Cadastrar",
    command=salvar_nome
  
)
botao_cadastrar.pack()
botao_listar = tk.Button(
    janela,
    text="Ver Cadastros",
    command=mostrar_cadastros
)
botao_listar.pack(pady=5)

resultado = tk.Label(
    janela,
    text="",
    justify="left"
)
resultado.pack(pady=20)

janela.mainloop()
 #deus funciona, eu estou a tanto tempo tentando entender isso, mas o importante é que funcione, né? :D
#EU ESQUECI DE MOSTRAR O BOTÃO DE VER CADASTROS, MAS AGORA ESTÁ LÁ, FUNCIONANDO PERFEITAMENTE. O IMPORTANTE É QUE FUNCIONE, NÉ? :D