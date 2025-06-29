import sqlite3
import random
import string
import os
from flask import Flask, request, redirect, render_template_string, flash

# --- Configuration Management: Get DB path from environment variable or default ---
# Set a secret key for flash messages 
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'a_very_secret_key_for_dev_only')
DB = os.environ.get('DATABASE_URL', 'urls.db')

# --- Helper function to initialize the database ---
def init_db():
    conn = None
    try:
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                short TEXT UNIQUE NOT NULL,
                long TEXT NOT NULL
            )
        ''')
        conn.commit()
        print(f"Database initialized at {DB}")
    except sqlite3.Error as e:
        print(f"ERROR: Database initialization failed: {e}")
    finally:
        if conn:
            conn.close()

# --- HTML template for the form and flash messages ---
# Moved out for readability and to allow re-rendering with flash messages
FORM_HTML = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Shortener</title>
    <style>
        body { font-family: sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { text-align: center; color: #333; }
        .flashes { list-style: none; padding: 0; margin-bottom: 20px; }
        .flashes li { padding: 10px 15px; margin-bottom: 10px; border-radius: 5px; }
        .flashes .error { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .flashes .success { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        form { display: flex; flex-direction: column; gap: 15px; }
        input[type="text"], input[type="url"] { padding: 10px; border: 1px solid #ddd; border-radius: 4px; font-size: 16px; }
        input[type="submit"] { background-color: #007bff; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; }
        input[type="submit"]:hover { background-color: #0056b3; }
        a { color: #007bff; text-decoration: none; }
        a:hover { text-decoration: underline; }
        .center-text { text-align: center; }
    </style>
</head>
<body>
    <h1>Shorten Your URL</h1>

    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <ul class=flashes>
        {% for category, message in messages %}
          <li class="{{ category }}">{{ message | safe }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}

    <form method="post">
        <label for="long_url">Long URL:</label>
        <input type="url" name="long_url" id="long_url" placeholder="e.g., https://www.example.com/very/long/path" required>
        <input type="submit" value="Shorten URL">
    </form>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("INSERT INTO urls (short, long) VALUES (?, ?)", (short, long_url))
        conn.commit()
        conn.close()
        return f"Short URL: <a href='/{short}'>localhost:5000/{short}</a>"
    return '''<form method="post">
                Long URL: <input name="long_url">
                <input type="submit">
              </form>'''

@app.route('/<short>')
def redirect_short(short):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT long FROM urls WHERE short = ?", (short,))
    result = c.fetchone()
    conn.close()
    if result:
        return redirect(result[0])
    return "URL not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
