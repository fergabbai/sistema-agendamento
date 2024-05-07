import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('agenda.db')  # Conecta ao banco de dados (cria se não existir)
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agendamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                data_horario DATETIME NOT NULL UNIQUE
            )
        ''')
        self.conn.commit()

    def verificar_disponibilidade(self, data_horario):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT COUNT(*) FROM agendamentos WHERE data_horario = ?
        ''', (data_horario,))
        resultado = cursor.fetchone()[0]
        return resultado == 0  # True se não houver agendamentos nesse horário

    def agendar_horario(self, cliente, data_horario):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO agendamentos (cliente, data_horario) VALUES (?, ?)
        ''', (cliente, data_horario))
        self.conn.commit()

    def desmarcar_horario(self, data_horario):
        cursor = self.conn.cursor()
        cursor.execute('''
            DELETE FROM agendamentos WHERE data_horario = ?
        ''', (data_horario,))
        self.conn.commit()
        return cursor.rowcount > 0  # True se algum registro foi deletado

    def obter_agenda(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT cliente, data_horario FROM agendamentos ORDER BY data_horario
        ''')
        resultados = cursor.fetchall()
        agenda = [{'cliente': r[0], 'data_horario': r[1].strftime("%d/%m/%Y %H:%M")} for r in resultados]
        return agenda