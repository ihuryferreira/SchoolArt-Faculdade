"""
ALUNO: MANUEL E ENRI

"""
import sqlite3
from sqlite3.dbapi2 import Error
from tkinter.constants import NONE
from conexao import Conexao

class Aluno:

    def cadastrar(self,nome,idade,cpf,matricula,email,endereco):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO aluno (nome,idade,cpf,matricula,email,endereco) VALUES (?,?,?,?,?,?)'
            cursor.execute(sql,(nome,idade,cpf,matricula,email,endereco))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de aluno: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False

    
    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
         
        
        try:
            resultset = cursor.execute('SELECT * FROM aluno ORDER BY nome').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")
            
        cursor.close()
        conexao.close()
        return resultset

    def buscar(self,name):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()
         
        
        try:
            resultset = cursor.execute('SELECT * FROM aluno WHERE nome LIKE '%' ORDER BY nome', (name,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")
            
        cursor.close()
        conexao.close()
        return resultset
    
    def consultar_detalhes(self, id_aluno):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM aluno WHERE id = ?', (id_aluno,)).fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")


        cursor.close()
        conexao.close()
        return resultset


    def consultar_ultimo_id(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset = cursor.execute('SELECT MAX(id) FROM aluno').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def atualizar(self,id_aluno,nome,idade,cpf,matricula,email,endereco):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE aluno SET nome = ?, idade = ?, cpf = ?, matricula = ?, email = ?, endereco = ? WHERE id = (?)'
            cursor.execute(sql,(nome,idade,cpf,matricula,email,endereco,id_aluno))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de aluno: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def excluir(self,id_aluno):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM aluno WHERE id = (?)'
            cursor.execute(sql,[id_aluno])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de aluno: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def consultar_por_matricula(self,matri):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT e.id, e.nome, e.idade, e.cpf, e.matricula, e.email, e.endereco 
                FROM aluno as e 
                WHERE matricula = ?"""

        resultset = None
        try:
            resultset =  cursor.execute(sql,(matri,)).fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset

            