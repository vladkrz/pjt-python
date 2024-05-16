from tkinter import *
import tkinter.filedialog

#Inicia a Instância Tk
root = Tk()

# Cria um widget de texto que será atrelado a widget principal(root)
text=Text(root)

""" 
    Usando o gerenciador de widgets grid, podemos gerar campos como um campo de texto
    A estrutura grid é mais fácil dos gerenciadores de widgets
    pois se utiliza de um estilo linha | coluna para organizar os widgets

"""
text.grid()

# Com método wm_title alteramos o nome da janela do programa
root.wm_title("Sted by VladKrz")

# Função para permitir salvar o que escrevemos no campo de texto em um arquivo
def saveAs():
    global text
    # Obtem  do inicio ao fim o que foi digitado no Widget Text da variável text
    t = text.get("1.0", "end-1c")
    # Pergunta onde quer salvar o arquivo por padrão de qualquer tipo
    saveLocation=tkinter.filedialog.asksaveasfilename()
    # Abre um arquivo no modo escrita, caso não exista, criará um
    file1 = open(saveLocation, "w+")
    # Irá escrever o conteúdo digitado na variável text (Widget TextBox)
    file1.write(t)
    # Fecha o arquivo 
    file1.close()

# Cria um botão para salvar o arquivo. command recebe uma função para ativar
button = Button(root, text="Save", command=saveAs)
button.grid()

def fontHelvetica():
    global text
    # Função que modifica o texto que aparecerá na Widget TextBox
    text.config(font="Helvetica")

def fontCourier():
    global text
    # Função que modifica o texto que aparecerá na Widget TextBox
    text.config(font="Courier")

# Cria um menu suspenso
font=Menubutton(root, text="Font")
font.grid()
""" 
    Associa as opcoes do menu suspenso ao botão Menu e 
    Remove a linha pontilhada acima das opções do menu suspenso
"""
font.menu=Menu(font, tearoff=0)
# Gera as opções no menu suspenso
font["menu"]=font.menu
"""
    Criação de duas variaveis de ligação com as opções criadas pelo add_checkbutton
    para monitorar a interação do usuário que altera o valor booleano de helvetica e courier
    através do variable=helvetica ou courier que receberam IntVar()(para valores inteiros)
"""
helvetica=IntVar()
courier=IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=fontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=fontHelvetica)

# Mantém o programa em execução
root.mainloop()