import sqlite3

class Conexao:

    def conectar(self):
        conexao = None
        db_path = 'school.db'
        try:
            conexao = sqlite3.connect(db_path, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

        except sqlite3.DatabaseError as err:
            print(f"Erro ao conectar o banco de dados {db_path}.")
        return conexao


    def createTableDisciplina(self,conexao,cursor):
        cursor.execute('DROP TABLE IF EXISTS Disciplina')

        sql = """CREATE TABLE IF NOT EXISTS Disciplina (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    codigo varchar NOT NULL,
                    disciplina varchar NOT NULL);"""

        cursor.execute(sql)
        conexao.commit()

    def createTables(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        self.createTableDisciplina(conexao,cursor)