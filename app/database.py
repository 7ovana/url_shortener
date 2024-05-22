import sqlite3 as sql
from pydantic import BaseModel


def initialize_db():
    conn = sql.connect("urls.db")
    c = conn.cursor()
    c.execute(
        """
            CREATE TABLE IF NOT EXISTS url_map (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target_url TEXT NOT NULL,
            short_url TEXT NOT NULL UNIQUE
            )
        """
    )
    conn.commit()
    conn.close()


def get_db_connection():
    conn = sql.connect("urls.db")
    conn.row_factory = sql.Row
    return conn


# class URLDB(BaseModel):
#     target_url: str
#     short_url: str
#     is_active: bool = True
#     clicks: int = 0
