"""
ALUNO: IHURY E FELIPE

"""
import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Discipliana:

    def cadastrar(self, id, disciplina):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO disciplina (id, disciplina) VALUES (?,?)'
            cursor.execute(sql,(id, disciplina))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de Disciplinas: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM disciplina').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    def consultar_detalhes(self, id):  
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute('SELECT * FROM disciplina WHERE id = ?', (id,)).fetchone()
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
            resultset = cursor.execute('SELECT MAX(id) FROM disciplina').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def atualizar(self,id, disciplina):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE disciplina SET codigo = ? WHERE id = (?)'
            cursor.execute(sql,(disciplina,id))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de disciplinas: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False


    def excluir(self,id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM disciplina WHERE id = (?)'
            cursor.execute(sql,[id])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de disciplina: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False