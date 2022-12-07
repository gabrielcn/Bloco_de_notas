import tkinter as tk
from tkinter import filedialog

# Criar a janela principal
janela = tk.Tk()
janela.title("Bloco de notas")

# Criar o widget de texto
texto = tk.Text(janela)
texto.pack()

# Criar funções para salvar e abrir arquivos
def salvar_arquivo():
    # Exibir diálogo de salvar arquivo
    arquivo = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if arquivo is None: # Se o usuário cancelar o diálogo, não fazer nada
        return
    # Obter o conteúdo do widget de texto e escrever no arquivo
    conteudo = texto.get("1.0", tk.END)
    arquivo.write(conteudo)
    arquivo.close()

def abrir_arquivo():
    # Exibir diálogo de abrir arquivo
    arquivo = filedialog.askopenfile(mode='r', defaultextension=".txt")
    if arquivo is None: # Se o usuário cancelar o diálogo, não fazer nada
        return
    # Limpar o widget de texto e ler o conteúdo do arquivo
    texto.delete("1.0", tk.END)
    conteudo = arquivo.read()
    texto.insert("1.0", conteudo)
    arquivo.close()

# Criar os botões de salvar e abrir
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_arquivo)
botao_salvar.pack(side=tk.LEFT)
botao_abrir = tk.Button(janela, text="Abrir", command=abrir_arquivo)
botao_abrir.pack(side=tk.LEFT)

# Iniciar o loop principal do tkinter
janela.mainloop()
