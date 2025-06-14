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
