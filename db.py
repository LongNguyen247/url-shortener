import sqlite3

DB_NAME = "urls.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short TEXT UNIQUE,
            long TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def save_url(short, long_url):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO urls (short, long) VALUES (?, ?)", (short, long_url))
    conn.commit()
    conn.close()


def get_url(short):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT long FROM urls WHERE short = ?", (short,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None
