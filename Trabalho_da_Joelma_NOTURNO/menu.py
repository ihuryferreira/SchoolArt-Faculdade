"""
ALUNO: IHURY E FELIPE

"""
#from tkinter import *
import tkinter as tk
import ttips

from PIL import Image, ImageTk

from aluno_win import Alunowin
from disciplina_view import PrincipalRAD
from registro_Nota_view import PrincipalRAD3


class MenuRAD:
    def __init__(self, window):
        princip = window
        self.principal1 = window
        self.tela = tk.Frame(princip, borderwidth=1, relief='solid')
        self.tela.place(x=5, y=5, width=55, height=780)

        self.ico = tk.StringVar()

        #Imagem = Tela do Manuel
        self.img = tk.PhotoImage(file='imagem/alunoIco.png')
        #Imagem = Tela do IHURY
        self.img1 = Image.open(r'imagem/disciplina.png')
        self.img2 = ImageTk.PhotoImage(self.img1)
        #Imagem = Tela do Kesio
        self.img3 = Image.open(r'imagem/formatua1.png')
        self.img4 = ImageTk.PhotoImage(self.img3)
        #Imagem = Fechar o Sistema
        self.close = Image.open(r'imagem/desligar.png')
        self.close2 = ImageTk.PhotoImage(self.close)

        self.MenuTitulo = tk.Label(self.tela, text='Menu', fg='red')
        self.MenuTitulo.place(x=5, y=10)
        
        self.bntCliclar = tk.Button(self.tela, image=self.img, command=self.Tela1)
        self.bntCliclar.place(x=5, y=55)
        ttips.Create(self.bntCliclar, 'Tela do MANUEL E ENRI')

        self.bntCliclar2 = tk.Button(self.tela, image=self.img2, command=self.Tela2)
        self.bntCliclar2.place(x=4, y=120)
        ttips.Create(self.bntCliclar2, 'Tela do IHURY E FELIPE')
        
        self.bntCliclar3 = tk.Button(self.tela, image=self.img4, command=self.Tela3)
        self.bntCliclar3.place(x=5, y=190)
        ttips.Create(self.bntCliclar3, 'Tela do KESIO E WELINGTON')

        self.Exit = tk.Button(self.tela, image=self.close2, command=princip.destroy)
        self.Exit.place(x=5, y=250)
        ttips.Create(self.Exit, 'Fechar o Sistema!')
        
    def Tela3(self):
        janela3 = tk.Toplevel()
        principal2 = PrincipalRAD3(janela3)
        janela3.title('Cadastro de Notas')
        janela3.geometry("1350x650+0+0")
        janela3.configure(background="#292826")
        #imagem_3 = ImageTk.PhotoImage(file="Art1.png")
        #tk.Label(janela3,image=imagem_3 ,bg='#292826',pady=0,).place(x=5,y=0,)
        janela3.iconbitmap("Artc.ico")
        janela3.mainloop()
    
    def Tela2(self):
        janela = tk.Toplevel()
        principal=PrincipalRAD(janela)
        janela.title('Cadastro de Disciplina')
        janela.geometry("740x650+0+0")
        janela.configure(background="#292826")
        imagem_ = ImageTk.PhotoImage(file="Art1.png")
        tk.Label(janela,image=imagem_ ,bg='#292826',pady=0,).place(x=5,y=0,)
        janela.iconbitmap("Artc.ico")
        janela.mainloop()

    def Tela1(self):
        janela2 = tk.Toplevel()
        principal2 = Alunowin(janela2)
        janela2.title('Cadastro de Aluno')
        janela2.geometry("950x650+0+0")
        janela2.configure(background="#292826")
        imagem_2 = ImageTk.PhotoImage(file="Art1.png")
        tk.Label(janela2,image=imagem_2 ,bg='#292826',pady=0,).place(x=5,y=0,)
        janela2.iconbitmap("Artc.ico")
        janela2.mainloop()