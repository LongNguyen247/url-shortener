from flask import Flask, request, redirect, render_template
import string, random, sqlite3

app = Flask(__name__)
DB = 'urls.db'

# Setup DB
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short TEXT UNIQUE,
            long TEXT
        )
    """)
    conn.commit()
    conn.close()
