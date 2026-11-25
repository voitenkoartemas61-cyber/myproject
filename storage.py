import sqlite3

DB = "data.db"


def connect():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


def init():
    with connect() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                note TEXT
            )
        """)


def load(category=None):
    with connect() as conn:
        if category is None:
            rows = conn.execute("SELECT * FROM items ORDER BY date").fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM items WHERE category = ? ORDER BY date",
                (category,)
            ).fetchall()
    return [dict(row) for row in rows]


def add(date, category, amount, note):
    with connect() as conn:
        cur = conn.execute(
            "INSERT INTO items (date, category, amount, note) VALUES (?, ?, ?, ?)",
            (date, category, amount, note)
        )
        return cur.lastrowid


def delete(item_id):
    with connect() as conn:
        cur = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
        return cur.rowcount > 0
