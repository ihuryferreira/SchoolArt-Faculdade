"""
ALUNO: Kesio, WELINTON E IHURY

"""
import sqlite3
from sqlite3.dbapi2 import Error
from conexao import Conexao

class Nota:

    def cadastrar(self,fk_disciplina_id, av1, av2, av3, media, situacao, fk_aluno_id):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'INSERT INTO nota (fk_disciplina_id, av1, av2, av3, media, situacao, fk_aluno_id) VALUES (?,?,?,?,?,?,?)'
            cursor.execute(sql,(fk_disciplina_id, av1,av2,av3,media,situacao, fk_aluno_id))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro no cadastro de Notas: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de integridade: {}".format(e))
            return False


    def consultar(self):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        try:
            resultset =  cursor.execute('SELECT * FROM nota').fetchall()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset


    def consultar_detalhes(self, id_nota):  
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()


        try:
            resultset =  cursor.execute('SELECT * FROM nota WHERE id_nota = ?', (id_nota,)).fetchone()
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
            resultset = cursor.execute('SELECT MAX(id_nota) FROM nota').fetchone()
        except Error as e:
            print(f"O erro '{e}' ocorreu.")

        
        cursor.close()
        conexao.close()
        return resultset[0]


    def atualizar(self,id_nota,av1, av2, av3, media, situacao):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'UPDATE nota SET id_nota = ? WHERE id = (?)'
            cursor.execute(sql,(situacao,media,av3,av2,av1,id_nota))
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na atualização de Notas: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False


    def excluir(self,id_nota):
        try:
            conn = Conexao()
            conexao = conn.conectar()
            cursor = conexao.cursor()

            sql = 'DELETE FROM nota WHERE id = (?)'
            cursor.execute(sql,[id_nota])
           
            conexao.commit()
            cursor.close()
            conexao.close()

            return True
        except sqlite3.OperationalError as e:
            print("Erro na exclusão de Notas: {}".format(e))
            return False
        except sqlite3.IntegrityError as e:
            print("Erro de inegridade: {}".format(e))
            return False

    def consultar_por_disciplina(self, fk_disciplina_id):
        conn = Conexao()
        conexao = conn.conectar()
        cursor = conexao.cursor()

        sql = """SELECT p.fk_aluno_id, p.fk_disciplina_id, p.id_nota, p.av1, p.av2, p.av3, p.media, p.situacao 
                    FROM nota as p
                    WHERE fk_disciplina_id = ?"""

        try:
            resultset =  cursor.execute(sql,[fk_disciplina_id]).fetchall()
        except sqlite3.Error as e:
            print(f"O erro '{e}' ocorreu.")

        cursor.close()
        conexao.close()
        return resultset