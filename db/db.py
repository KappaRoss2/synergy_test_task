import sqlite3
from typing import List, Dict


class Database:
    """Класс для работы с БД."""

    _columns = {
        'id': 'INTEGER PRIMARY KEY',
        'username': 'TEXT',
        'followees': 'INTEGER',
        'followers': 'INTEGER',
        'mediacount': 'INTEGER',
        'biography': 'TEXT',
        'full_name': 'TEXT',
    }

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def table_exists(self, table_name: str) -> bool:
        self.cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name=?', (table_name,))
        return bool(self.cursor.fetchone())

    def create_table(self, table_name: str):
        if not self.table_exists(table_name):
            column_definitions = ', '.join([f'{col_name} {col_type}' for col_name, col_type in self._columns.items()])
            query = f'CREATE TABLE {table_name} ({column_definitions})'
            self.cursor.execute(query)
            self.conn.commit()

    def insert_data(self, table_name: str, data: List[Dict[str, any]]):
        if not data:
            return
        columns = ', '.join(data[0].keys())
        placeholders = ', '.join(['?'] * len(data[0]))
        query = f'INSERT INTO {table_name} ({columns}) VALUES ({placeholders})'
        values = [tuple(row.values()) for row in data]
        self.cursor.executemany(query, values)
        self.conn.commit()
