"""
ALUNO: KESIO E WELINTO

"""

import tkinter as tk
from tkinter import ttk
#from pandas import pd
from tkinter import messagebox as mb
from tkinter.constants import DISABLED, END, NORMAL

from aluno import Aluno
from disciplina import Discipliana

from gravarDados import Nota

class PrincipalRAD3:
    def __init__(self,win):
        self.notaCRUD = Nota()
        self.deptSelected = None
        self.selected_aluno = 0
        #Aqui ira Buscar a Disciplina
        self.lblDisciplina = tk.Label(win, text='Disciplina:')
        self.txtDisciplina = ttk.Combobox(win,values=[])
        self.lblDisciplina.place(x=10, y=10)
        self.txtDisciplina.place(x=75, y=10)
        self.txtDisciplina.bind("<<ComboboxSelected>>", self._on_combo_changed)
        self.popular_combo_disciplina()


        self.frame = tk.Frame(win, borderwidth=4, relief='sunken')
        self.frame.place(x=100, y=100, width=800, height=150)

        self.Titulo = tk.Label(self.frame, text='Cadastrar Notas', fg='red')
        self.lblNota1=tk.Label(self.frame, text='AV1')
        self.lblNota2=tk.Label(self.frame, text='AV2')
        self.lblNota3=tk.Label(self.frame, text='AV3')
        self.lblMedia=tk.Label(self.frame, text='Média')
        self.txtNota1=tk.Entry(self.frame, bd=3)
        self.txtNota2=tk.Entry(self.frame, bd=3)
        self.txtNota3=tk.Entry(self.frame, bd=3)
        self.txtAluno=tk.Entry(self.frame, bd=3)
        self.btnCalcular=tk.Button(self.frame, text='Calcular Média', command=self.fSalvarDados)
        #Buscar Aluno
        self.frametexto = tk.Frame(win)
        self.frametexto.pack()
        self.lblNome=tk.Label(win, text='Matricula:')
        self.txtmatricula=tk.Entry(win,bd=3, width=29)
        #self.NomedoAluno=tk.Label(win, text='Nome do Aluno:')
        self.btnBuscarCodigo=tk.Button(win, text='Buscar Codigo', command=(lambda : self.buscar(self.txtmatricula.get())))
        # Treview aluno
        self.dadosAluno = ('ALUNO')

        self.treeMedias2 = ttk.Treeview(win, columns=self.dadosAluno, show='headings')
        self.verscrlbar2 = ttk.Scrollbar(win, orient='vertical', command=self.treeMedias2.yview)
        self.verscrlbar2.pack(side='left', fill='x')
        self.treeMedias2.configure(yscrollcommand=self.verscrlbar2.set)
        self.treeMedias2.heading("ALUNO", text="Nome do Aluno")
        self.treeMedias2.column("ALUNO",minwidth=0,width=100)
        self.treeMedias2.pack(padx=100, pady=5)
        self.treeMedias2.place(x=250, y=43, width=300, height=50)# rever e da uma olhada
        self.verscrlbar2.place(x=552, y=45, height=43)# Não esquecer de Mudar
        #----- Componente TreeView --------------------------------------------
        self.dadosColunas = ("ID", "AV1", "AV2", 'AV3', "Média", "Situação")         
        
        
        self.treeMedias = ttk.Treeview(win, 
                                       columns=self.dadosColunas,
                                       show='headings')
        #self.treeMedias = ttk.Treeview(win, columns=(1,2,3,4,5,6), show='headings')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeMedias.yview)
        
        self.verscrlbar.pack(side ='left', fill ='x')
                
        
        
        self.treeMedias.configure(yscrollcommand=self.verscrlbar.set)
        
        #self.treeMedias.heading("ID", text="ID")
        self.treeMedias.heading("ID", text="ID")
        self.treeMedias.heading("AV1", text="AV1")
        self.treeMedias.heading("AV2", text="AV2")
        self.treeMedias.heading('AV3', text='AV3')
        self.treeMedias.heading("Média", text="Média")
        self.treeMedias.heading("Situação", text="Situação")
        

        #self.treeMedias.column("ID",minwidth=0,width=100)
        self.treeMedias.column("ID",minwidth=0,width=100)
        self.treeMedias.column("AV1",minwidth=0,width=100)
        self.treeMedias.column("AV2",minwidth=0,width=100)
        self.treeMedias.column('AV3', minwidth=0,width=100)
        self.treeMedias.column("Média",minwidth=0,width=100)
        self.treeMedias.column("Situação",minwidth=0,width=100)

        self.treeMedias.pack(padx=10, pady=10)
                
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #--------------------------------------------------------------------- 
        self.lblNome.place(x=250, y=10)
        self.txtmatricula.place(x=315, y=10)

        #self.NomedoAluno.place(x=250, y=47)
       
        #Cadastrar Notas
        self.Titulo.place(x=350, y=20)
        self.lblNota1.place(x=35, y=60)
        self.txtNota1.place(x=89, y=60)
        
        self.lblNota2.place(x=230, y=60)
        self.txtNota2.place(x=280, y=60)

        self.lblNota3.place(x=430, y=60)
        self.txtNota3.place(x=480, y=60)

        self.txtAluno.place(x=310, y=104)

        self.btnCalcular.place(x=620, y=58)
        # Fim do Cadastro

        self.btnBuscarCodigo.place(x=500, y=6)
           
        self.treeMedias.place(x=100, y=300, width=1100)# rever e da uma olhada
        self.verscrlbar.place(x=1193, y=300, height=225)# Não esquecer de Mudar
        
        
        #self.id = 0
        #self.iid = 0

        self.carregarDadosIniciais2()

    def popular_combo_disciplina(self):
        discipl = Discipliana()
        self.deptResult = discipl.consultar()
        if (len(self.deptResult)>0):

            self.deptSelected = self.deptResult[0][0]

            for registro in self.deptResult:
                self.txtDisciplina['values'] = (*self.txtDisciplina['values'], registro[1])
            
            self.txtDisciplina.current(0)

    def carregarDadosIniciais2(self):
        #  registros = self.notaCRUD.consultar()
        if (self.deptSelected != None):
            resultado = self.notaCRUD.consultar_por_disciplina(self.deptSelected)
            self.treeMedias.delete(*self.treeMedias.get_children())
            count = 0
            for item in resultado:
                #data_em_texto = '{}/{}/{}'.format(registro[2].day, registro[2].month, registro[2].year)
                self.treeMedias.insert('', 'end',
                                   iid=count,                                   
                                   values=(str(item[2]),
                                           str(item[3]),
                                           str(item[4]),
                                           str(item[5]),
                                           str(item[6]),
                                           item[7],
                                           str(item[1])))
            
            
                #self.iid = self.iid + 1
                count = count + 1 

#-----------------------------------------------------------------------------
#Salvar dados para Banco e Treview
#-----------------------------------------------------------------------------           
    def fSalvarDados(self):
        aluno = self.txtAluno.get()
        av1 = float(self.txtNota1.get())
        av2 = float(self.txtNota2.get())
        av3=float(self.txtNota3.get())
        media, situacao = self.fVerificarSituacao(av1, av2, av3)

        if  self.notaCRUD.cadastrar(self.deptSelected, av1, av2, av3, media, situacao, aluno):
            numeroLinhas = len(self.treeMedias.get_children())
            id = self.notaCRUD.consultar_ultimo_id()

            self.treeMedias.insert('', 'end',
                                    iid=numeroLinhas,
                                    values=(str(id),
                                            str(av1),
                                            str(av2),
                                            str(av3),
                                            str(media),
                                            situacao, str(aluno)))
            
            mb.showinfo("Mensagem", "Cadastro executado com sucesso.")
            #self.txtmatricula.delete(0, tk.END)
            self.txtNota1.delete(0, tk.END)
            self.txtNota2.delete(0, tk.END)
            self.txtNota3.delete(0, tk.END)
        else:
            mb.showerror('Erro', 'Não Foi posivel Cadastrar.')
            #self.txtmatricula.focus_set()
            self.txtNota1.focus_set()
            self.txtNota2.focus_set()
            self.txtNota3.focus_set()

#-----------------------------------------------------------------------------
#calcula a média e verifica qual é a situação do aluno
#-----------------------------------------------------------------------------          
    def fVerificarSituacao(self, av1, av2, av3):
          media=(av1+av2+av3)/3
          if(media>=6.0):
             situacao = 'Aprovado'
          elif(media>=5.0):
              situacao = 'Em Recuperação'
          else:   
             situacao = 'Reprovado'
         
          return media, situacao

    def _on_combo_changed(self, event):
        index = self.txtDisciplina.current()
        self.deptSelected = self.deptResult[index][0]
        self.carregarDadosIniciais2()

    def delet_campos(self):
        self.txtmatricula.delete(0, tk.END)

    def carregar_dados_iniciais_treeView3(self):
        self.alunoCRUD = Aluno()
        self.treeMedias2.delete(*self.treeMedias2.get_children())
        self.delet_campos()
        registro = self.alunoCRUD.consultar()

        count = 0
        for item in registro:
            nome = item[1]
            matricula = item[4]

            self.treeMedias2.insert('','end',iid=count,values=(str(matricula),nome))
            count = count + 1

    def _on_click_placehold2(self, event):
        self.buscaEdit.configure(state=NORMAL)
        self.buscaEdit.delete(0, END)

    def placehold2(self):
        self.txtmatricula.insert(0, 'Digite sua Matricula')
        self.txtmatricula.configure(state=DISABLED)
        self.txtmatricula.bind('<Button-1>', self._on_click_placehold2)

    def buscar(self,event):
        self.alunoCRUD = Aluno()
        if self.txtmatricula.get()=="" or self.txtmatricula.get()==str('Digite sua Matricula'):
            mb.showinfo("Erro","Digite sua Matricula no Campo Busca!")
        
        else:
            #deleta lista ao click
            self.treeMedias2.delete(*self.treeMedias2.get_children())
                
            #obtem a entrada digitada pelo usuario no campo busca e coloca em uma lista
            lista = self.alunoCRUD.consultar_por_matricula(self.txtmatricula.get())
            item = self.treeMedias2.selection()    
            for item in lista:
                nome = item[1]
                aluno = item[4]
                #deleta os campos prenchidos do formulario
                self.delet_campos()
            try:
                self.txtAluno.insert(0, aluno)
                self.treeMedias2.insert('','end',values=(nome))
                self.txtmatricula.delete(0, tk.END)
                #self.placehold2()
            except:
                mb.showinfo("Erro", "Aluno nao cadastrado no banco de dados")
                self.placehold2()
                self.carregar_dados_iniciais_treeView3()

#janela=tk.Tk()
#principal=PrincipalRAD3(janela)
#janela.title('Registro de Notas')
#janela.geometry("1300x680+10+10")
#janela.mainloop()