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

# --- Helper function to initialise the database ---
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

# --- Route 1: Main Page (URL Shortening Form) ---
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form.get('long_url')

        # --- Input Validation ---
        if not long_url:
            flash('Please enter a URL to shorten.', 'error')
            return render_template_string(FORM_HTML)
        # Simple validation: checks if it starts with http(s)://
        if not (long_url.startswith('http://') or long_url.startswith('https://')):
            flash('Please enter a valid URL starting with http:// or https://.', 'error')
            return render_template_string(FORM_HTML)

        short = None
        MAX_RETRIES = 5  # Max attempts to find a unique short code
        for _ in range(MAX_RETRIES):
            potential_short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            try:
                # --- Short Code Collision Handling (Check for existing code) ---
                with sqlite3.connect(DB) as conn:
                    c = conn.cursor()
                    c.execute("SELECT 1 FROM urls WHERE short = ?", (potential_short,))
                    if not c.fetchone():  # If the short code does not exist
                        short = potential_short
                        break # Found a unique code, exit loop
            except sqlite3.Error as e:
                flash(f"An internal database error occurred while checking short code uniqueness: {e}", 'error')
                return render_template_string(FORM_HTML)

        if not short:
            flash("Failed to generate a unique short URL. Please try again.", 'error')
            return render_template_string(FORM_HTML)

        try:
            # --- Database Insertion with Error Handling ---
            with sqlite3.connect(DB) as conn:
                c = conn.cursor()
                c.execute("INSERT INTO urls (short, long) VALUES (?, ?)", (short, long_url))
                conn.commit()
            # --- User Feedback (Flash Message) ---
            flash(f"Short URL created: <a href='/{short}'>http://localhost:5000/{short}</a>", 'success')
            return redirect('/') # Redirect to clear the form and display messages
        except sqlite3.IntegrityError:
            # This specific error might occur if two requests try to insert the same short code concurrently
            flash("A URL with this short code already exists. Please try again.", 'error')
            return render_template_string(FORM_HTML)
        except sqlite3.Error as e:
            flash(f"An internal database error occurred: {e}", 'error')
            return render_template_string(FORM_HTML)

    return render_template_string(FORM_HTML)

# --- Route 2: Short URL Redirection ---
@app.route('/<short>')
def redirect_short(short):
    try:
        # --- Database Lookup with Error Handling ---
        with sqlite3.connect(DB) as conn:
            c = conn.cursor()
            c.execute("SELECT long FROM urls WHERE short = ?", (short,))
            result = c.fetchone()

        if result:
            return redirect(result[0])
        else:
            # --- Improved 404 Page ---
            return render_template_string('''
                <!doctype html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>URL Not Found</title>
                    <style>
                        body { font-family: sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; }
                        h1 { color: #dc3545; }
                        p { color: #6c757d; }
                        a { color: #007bff; text-decoration: none; }
                        a:hover { text-decoration: underline; }
                    </style>
                </head>
                <body>
                    <h1>404 - URL Not Found</h1>
                    <p>The short URL you entered does not exist or has expired.</p>
                    <p><a href='/'>Go back to shorten a new URL</a></p>
                </body>
                </html>
            '''), 404
    except sqlite3.Error as e:
        print(f"ERROR: Database error during redirection for short code '{short}': {e}")
        return render_template_string('''
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Internal Server Error</title>
                <style>
                    body { font-family: sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; border: 1px solid #ccc; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; }
                    h1 { color: #dc3545; }
                    p { color: #6c757d; }
                </style>
            </head>
            <body>
                <h1>500 - Internal Server Error</h1>
                <p>An unexpected error occurred. Please try again later.</p>
            </body>
            </html>
        '''), 500

# --- Main Execution Block ---
if __name__ == '__main__':
    init_db()
    # In a production environment, debug should be False  
    # and you would use a production-ready WSGI server like Gunicorn or uWSGI
    app.run(debug=True)
