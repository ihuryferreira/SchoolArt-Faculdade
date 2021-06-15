"""
ALUNO: MANUEL E ENRI

"""

from tkinter.constants import DISABLED, END, NORMAL
#from tkinter.font import BOLD, Font
#from typing import ItemsView, Sized
from aluno import Aluno
#from PIL import Image, ImageTk
#from tkinter import Event, Tk, tix
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb



class Alunowin:

    def __init__(self,win,):
        self.alunoCRUD = Aluno()
        vcmd = (win.register(self.no_str))
        yes = (win.register(self.yes_str))
        #Criar os componentes de tela
        self.alunoed2Label = tk.Label(win, text='_______________', background='#292826',foreground='#F1780e')
        self.alunoedLabel = tk.Label(win, text='______________________________________',background='#292826',foreground='#F1780e')
        self.alunoLabel = tk.Label(win, text='ALUNO',font="Bold 17", background='#292826',foreground='#F1780e')

        self.nomeLabel = tk.Label(win, text='* Nome',font="Bold 10", background='#292826',foreground='#F1780e') 
        self.nomeEdit = tk.Entry(win,width = 32, bd=1,bg='#dde',validate='all',validatecommand=(yes,'%S'))

        self.idadeLabel = tk.Label(win, text='Idade',font="Bold 10", background='#292826',foreground='#F1780e') 
        self.idadeEdit = tk.Entry(win,width = 32, bd=1,bg='#dde',validate='all',validatecommand=(vcmd,'%P'))

        self.cpfLabel = tk.Label(win, text='* CPF',font="Bold 10", background='#292826',foreground='#F1780e') 
        self.cpfEdit = tk.Entry(win,width = 32, bd=1,bg='#dde',validate='all',validatecommand=(vcmd,'%P'))
        
        self.matriculaLabel = tk.Label(win, text='* Matricula',font="Bold 10", background='#292826',foreground='#F1780e') 
        self.matriculaEdit = tk.Entry(win,width = 32, bd=1,bg='#dde',validate='all',validatecommand=(vcmd,'%P'))
        
        self.emailLabel = tk.Label(win, text='* E-mail',font="Bold 10", background='#292826',foreground='#F1780e') 
        self.emailEdit = tk.Entry(win,width = 32, bd=1,bg='#dde')

        self.enderecoLabel = tk.Label(win, text='Endereço',font="Bold 10", background='#292826',foreground='#F1780e') 
        self.enderecoEdit = tk.Entry(win,width = 32, bd=1,bg='#dde')
        #------------#
        # Boloes
        #------------#
        

        self.buscaEdit = tk.Entry(win,width=85, bd=1,bg='#dde')
        self.buscaEdit.insert(0, 'Digite sua Matricula')
        self.buscaEdit.configure(state=DISABLED)
        self.buscaEdit.bind('<Button-1>', self._on_click_placehold)
        self.buscaEdit.bind("<Return>",(lambda Event: self.buscar(self.buscaEdit.get())))
        
        #------------#
        # botoes s
        #------------#
        self.btnlista = tk.Button(win, 
        text='Lista',bg='#dde',command=self.carregar_dados_iniciais_treeView, bd=0)
        
        self.btnbusca = tk.Button(win, 
        text='Busca',bg='#dde',command=(lambda : self.buscar(self.buscaEdit.get())), bd=0)
        
        

        self.btnCadastrar = tk.Button(win, 
                text = 'Salvar',bg='#dde', width = 7, command=self._on_cadastrar_clicked, bd=1)

        self.btnAlterar = tk.Button(win, 
                text = 'Editar',bg='#dde', width = 7, command=self._on_atualizar_clicked, bd=1)

        self.btnExcluir = tk.Button(win, 
                text = 'Excluir',bg='#dde', width = 7, command=self._on_deletar_clicked, bd=1)
        

        self.alunoList = ttk.Treeview(win, columns=(1,2,3,4,5,6,7), show='headings')
        
        self.verscrlbar = ttk.Scrollbar(win,orient="vertical", command=self.alunoList.yview)
        self.verscrlbar.pack(side = 'right', fill='x')
        self.alunoList.configure(yscrollcommand = self.verscrlbar.set)

        self.alunoList.heading(1, text='ID')
        self.alunoList.heading(2, text='Nome')
        self.alunoList.heading(3, text='Idade')
        self.alunoList.heading(4, text='CPF')
        self.alunoList.heading(5, text='Matricula')
        self.alunoList.heading(6, text='E-mail')
        self.alunoList.heading(7, text='Endereço')
      
        

        self.alunoList.column(1, minwidth=0, width=0)
        self.alunoList.column(2, minwidth=0, width=200)
        self.alunoList.column(3, minwidth=0, width=45)
        self.alunoList.column(4, minwidth=0, width=100)
        self.alunoList.column(5, minwidth=0, width=100)
        self.alunoList.column(6, minwidth=0, width=150)
        self.alunoList.column(7, minwidth=0, width=200)

        
        self.alunoList.pack()
        self.alunoList.bind("<<TreeviewSelect>>", self._on_mostrar_clicked)
        

        #Posicionar os componentes na tela
        self.alunoed2Label.place(x=440,y=80)
        self.alunoedLabel.place(x=380,y=20)
        self.alunoLabel.place(x=440,y=50)

        self.nomeLabel.place(x=161,y=130)
        self.nomeEdit.place(x=220,y=130)
        
        self.idadeLabel.place(x=170,y=160)
        self.idadeEdit.place(x=220,y=160)

        self.emailLabel.place(x=161,y=190)
        self.emailEdit.place(x=220,y=190)

        self.cpfLabel.place(x=451,y=130)
        self.cpfEdit.place(x=530,y=130)
        
        self.matriculaLabel.place(x=451,y=160)
        self.matriculaEdit.place(x=530,y=160)

        self.enderecoLabel.place(x=460,y=190)
        self.enderecoEdit.place(x=530,y=190)

        self.buscaEdit.place(x=295,y=300)
        #--------
        # Posicionamnto dos Botoes
        #--------
        self.btnlista.place(x=865,y=298)
        self.btnbusca.place(x=820,y=298)
        self.btnCadastrar.place(x=670,y=250)
        self.btnAlterar.place(x=600,y=250)
        self.btnExcluir.place(x=530,y=250)
        self.alunoList.place(x=70,y=330)
        self.verscrlbar.place(x=880,y=330, height=230)

        self.carregar_dados_iniciais_treeView()
        #--------
        # Funções
        #--------
        
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

    
    def _on_click_placehold(self, event):
        self.buscaEdit.configure(state=NORMAL)
        self.buscaEdit.delete(0, END)
        #janela.unbind('<Button-1>')
        #fazendo unbind com root da janela especificando exatamente qual
        # a funçao deve ser realizada o unbind nao teremos o erro de string
    
    def placehold(self): 
        self.buscaEdit.insert(0, 'Digite sua Matricula')
        self.buscaEdit.configure(state=DISABLED)
        self.buscaEdit.bind('<Button-1>', self._on_click_placehold)

    def delet_campos(self):
        #deletar os campos dentros das Entry
        self.nomeEdit.delete(0, tk.END)
        self.idadeEdit.delete(0, tk.END)
        self.cpfEdit.delete(0, tk.END)
        self.matriculaEdit.delete(0, tk.END)
        self.emailEdit.delete(0, tk.END)
        self.enderecoEdit.delete(0, tk.END)
        self.buscaEdit.delete(0, tk.END)      

    def _on_mostrar_clicked(self, event):
        #Seleção do usuario, linha na qual ele clicou
        selection = self.alunoList.selection()
        item = self.alunoList.item(selection)
        nome = item["values"][1]
        idade = item["values"][2]
        cpf   = item["values"][3]
        matricula = item["values"][4]
        email = item["values"][5]
        endereco = item["values"][6]
        self.placehold()
        self.delet_campos()
        self.nomeEdit.insert(0, nome)
        self.idadeEdit.insert(0, idade)
        self.cpfEdit.insert(0, cpf)
        self.matriculaEdit.insert(0, matricula)
        self.emailEdit.insert(0, email)
        self.enderecoEdit.insert(0, endereco)

    def carregar_dados_iniciais_treeView(self):
        self.alunoList.delete(*self.alunoList.get_children())
        self.delet_campos()
        registro = self.alunoCRUD.consultar()

        count = 0
        for item in registro:
            id = item[0]
            nome = item[1]
            idade = item[2]
            cpf   = item[3]
            matricula = item[4]
            email = item[5]
            endereco = item[6]

            self.alunoList.insert('','end',iid=count,values=(str(id),nome,idade,cpf,matricula,email,endereco))
            count = count + 1
    
    def buscar(self,event):
        if self.buscaEdit.get()=="" or self.buscaEdit.get()==str('Digite sua Matricula'):
            mb.showinfo("Erro","Digite sua Matricula no Campo Busca!")
        
        else:
                #deleta lista ao click
                self.alunoList.delete(*self.alunoList.get_children())
                
                #obtem a entrada digitada pelo usuario no campo busca e coloca em uma lista
                lista = self.alunoCRUD.consultar_por_matricula(self.buscaEdit.get())
                item = self.alunoList.selection()       
                for item in lista:
                    id = item[0]
                    nome = item[1]
                    idade = item[2]
                    cpf   = item[3]
                    matricula = item[4]
                    email = item[5]
                    endereco = item[6]
                #deleta os campos prenchidos do formulario
                self.delet_campos()
                try:
                    self.alunoList.insert('','end',values=(str(id),nome,idade,cpf,matricula,email,endereco))
                    self.placehold()
                except:
                    mb.showinfo("Erro", "Aluno nao cadastrado no banco de dados")
                    self.placehold()
                    self.carregar_dados_iniciais_treeView()

    def _on_cadastrar_clicked(self):
        #Recuperar os dados dos campos texto
        nome = self.nomeEdit.get()
        idade = self.idadeEdit.get()
        cpf = self.cpfEdit.get()
        matricula = self.matriculaEdit.get()
        email = self.emailEdit.get()
        endereco = self.enderecoEdit.get()

        #Chamar o cadastrar do aluno.py para cadastrar no banco
        if self.cpfEdit.get()=="" or self.nomeEdit.get()=="":
                mb.showinfo("Campos em branco","Os campos com ( * ) não podem ficar vazio")
                
        else: 
                if self.alunoCRUD.cadastrar(nome,idade,cpf,matricula,email,endereco):
                    numeroLinha = len(self.alunoList.get_children())
                    id_aluno = self.alunoCRUD.consultar_ultimo_id()
                    self.alunoList.insert('','end',numeroLinha,values=(str(id_aluno),nome,idade,cpf,matricula,email,endereco))
                        #Mostrar mensagem para usuário
                    mb.showinfo("Mensagem", "Cadastro executado com sucesso!")
                        
                        #Limpar os campos texto
                    self.delet_campos()
                    
                else:
                    mb.showinfo("Mensagem", "Erro no cadastro!")
                    #Retornando o foco
                    self.nomeEdit.focus_set()
                    self.idadeEdit.focus_set()
                    self.cpfEdit.focus_set()
                    self.matriculaEdit.focus_set()
                    self.emailEdit.focus_set()
                    self.enderecoEdit.focus_set()


    def _on_atualizar_clicked(self):
        linha = self.alunoList.selection()
      
        if len(linha) != 0:
            id = self.alunoList.item(linha[0])["values"][0]
            nome = self.nomeEdit.get()
            idade = self.idadeEdit.get()
            cpf = self.cpfEdit.get()
            matricula = self.matriculaEdit.get()
            email = self.emailEdit.get()
            endereco = self.enderecoEdit.get()

            if  self.alunoCRUD.atualizar(id,nome,idade,cpf,matricula,email,endereco):

                self.alunoList.item(self.alunoList.focus(), values=(str(id),nome,idade,cpf,matricula,email,endereco))
                 #remover a seleção
                self.carregar_dados_iniciais_treeView()
                #----------#
                mb.showinfo("Mensagem", "Alteração executada com sucesso.")
                self.delet_campos()
            else:
                mb.showinfo("Mensagem", "Erro na alteração.")
                self.nomeEdit.focus_set()

    def _on_deletar_clicked(self):
        linhaSelecionada = self.alunoList.selection()

        if len(linhaSelecionada) != 0:
            id = self.alunoList.item(linhaSelecionada[0])["values"][0]

            if  self.alunoCRUD.excluir(id):
                self.alunoList.delete(linhaSelecionada)
                
                mb.showinfo("Mensagem", "Exclusão executada com sucesso.")
                self.delet_campos()
            else:
                mb.showinfo("Mensagem", "Erro na exclusão.")
                self.nomeEdit.focus_set()
                self.idadeEdit.focus_set()
                self.cpfEdit.focus_set()
                self.matriculaEdit.focus_set()
                self.emailEdit.focus_set()
                self.enderecoEdit.focus_set()   

    

#janela = tk.Tk()
#principal = Alunowin(janela)
#janela.title("Cadastro de Aluno")
#janela.geometry("950x650+0+0")
#janela.configure(background="#292826")
#imagem_ = ImageTk.PhotoImage(file="Art1.png")
#Label=Label(janela,image=imagem_,bg='#292826',pady=0,).place(x=5,y=0,)
#janela.iconbitmap("Artc.ico")
#janela.mainloop()