from tkinter import *

def funcClique():
    print ('Botão foi pressionado.')

janela = Tk()

frase = Label(master = janela, text = "Para observar o clique do botão, clique novamente.")
frase.pack()

botao = Button(master = janela, text = "Clique no botão", command = funcClique)
botao.pack()

janela.mainloop()
