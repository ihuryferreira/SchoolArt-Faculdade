"""
ALUNO: IHURY E FELIPE

"""
import tkinter as tk
import ttips
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.constants import TOP
from PIL import Image, ImageTk

from disciplina import Discipliana


class PrincipalRAD:
    def __init__(self,win):
        self.disciplinaCRUD = Discipliana()
        self.Titulo = tk.Label(win, text='Registro de Disciplina',font="Bold 17", background='#292826',foreground='#F1780e')
        self.Titulo.place(x=340, y=0)
        vcmd = (win.register(self.no_str))
        
        #componentes
        self.lblcodigo = tk.Label(win, text='Codigo:',font="Bold 17", background='#292826',foreground='#F1780e')
        self.lbldisciplina = tk.Label(win, text='Disciplina',font="Bold 17", background='#292826',foreground='#F1780e')
        self.txtcodigo = tk.Entry(win,bd=3,  validate='all',validatecommand=(vcmd,'%P'))
        ttips.Create(self.txtcodigo, 'Adiciona o número \nPara Cadastrar o Codigo da Disciplina!')
        self.txtdisciplina = tk.Entry(win,bd=3)
        ttips.Create(self.txtdisciplina, 'Adiciona o nome da Disciplina\nPara Cadastrar!')
        self.img = Image.open(r'imagem/pen.png')
        self.img2 = ImageTk.PhotoImage(self.img)
        #self.testepho = self.img.subsample(3,3) 
        self.btnResultado = tk.Button(win,
                text='Cadastrar', image=self.img2,compound='right', command=self.fSalvarDados)
        self.btnResultado.place(x=100, y=240)
        ttips.Create(self.btnResultado, 'Aperte Botão da imagem Lapis\n Para Cadastrar Codigo e a Disciplina')
        #----- Componente TreeView --------------------------------------------
        self.treeMedias = ("Codigo", "Disciplina")       
        
        
        self.treeMedias = ttk.Treeview(win, columns=(1,2), show='headings')
        
        self.verscrlbar = ttk.Scrollbar(win, 
                orient="vertical", command=self.treeMedias.yview)
        
        self.verscrlbar.pack(side ='left', fill ='x')        
        
        self.treeMedias.configure(yscrollcommand = self.verscrlbar.set)
        
        #self.treeMedias.heading(1, text="id")
        self.treeMedias.heading(1, text="Codigo")
        self.treeMedias.heading(2, text="Disciplina")
        

        self.treeMedias.column(1,minwidth=0,width=100)
        self.treeMedias.column(2,minwidth=0,width=100)
        #self.treeMedias.column(3,minwidth=0,width=100)

        self.treeMedias.pack()
        self.treeMedias.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)
                
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------        
        self.lblcodigo.place(x=84, y=130)
        self.txtcodigo.place(x=200, y=133)
        
        self.lbldisciplina.place(x=84, y=200)
        self.txtdisciplina.place(x=200, y=205)
           
        self.treeMedias.place(x=100, y=300)
        self.verscrlbar.place(x=305, y=300, height=225)
        
        self.carregarDadosIniciais()

#-----------------------------------------------------------------------------
    def no_str(self, P):
        #somente numeros
        if str.isdigit(P) or P=="":
            return True
        else:
            return False
    
    def yes_str(self, S):
        #somente caracter
        if str.isdigit(S):
            return False
        else:
            return True
#================================================================================
    def carregarDadosIniciais(self):
          registros = self.disciplinaCRUD.consultar()
          
          count = 0
          for item in registros:
              codigo = item[0]
              disciplina = item[1]

              self.treeMedias.insert('','end',iid=count, values=(str(codigo),disciplina))
              count = count + 1
            
#-----------------------------------------------------------------------------
#Salvar dados para uma planilha excel
#-----------------------------------------------------------------------------           
    def fSalvarDados(self):
        #Recuperar os dados dos campos texto
        codigo = self.txtcodigo.get()
        disciplina = self.txtdisciplina.get()

        #Chamar o cadastrar do disciplina.py para cadastrar no banco
        if self.disciplinaCRUD.cadastrar(codigo,disciplina) == True:
            id = self.disciplinaCRUD.consultar_ultimo_id()
            #Atualizar a TreeView
            self.treeMedias.insert('','end',iid=(id+1),values=(str(codigo),disciplina))

            #Mostrar mensagem para usuário
            mb.showinfo("Mensagem", "Cadastro executado com sucesso!")

            #Limpar os campos texto
            self.txtcodigo.delete(0,tk.END)
            #self.txtdisciplina.delete(1,tk.END)
        else:
            mb.showinfo("Mensagem", "Erro no cadastro!")
            #Retornando o foco
            self.txtcodigo.focus_set()
            self.txtdisciplina.focus_set()

    def _on_mostrar_clicked(self,codigo):
        self.txtcodigo.delete(0, tk.END)
        self.txtdisciplina.delete(0, tk.END)
        for selection in self.treeMedias.selection():
            item = self.treeMedias.item(selection)
            codigo = item['values'][0]
            disciplina = item['values'][1]
            self.txtcodigo.insert(0, codigo)
            self.txtdisciplina.insert(0, disciplina)

        
#-----------------------------------------------------------------------------
#Programa Principal
#-----------------------------------------------------------------------------          

#janela=tk.Tk()
#principal=PrincipalRAD(janela)
#janela.title('Bem Vindo ao Registro de Disciplina')
#janela.geometry("700x600+10+10")
#janela.iconbitmap("images.ico")
#janela.mainloop()
