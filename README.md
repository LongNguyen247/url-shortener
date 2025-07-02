# url-shortener

A lightweight and easy-to-use URL shortener built with Flask and SQLite. This project allows users to convert long URLs into concise, shareable short links and then redirects to the original URL when the short link is accessed.

## Features

* **URL Shortening:** Convert long, cumbersome URLs into short, random 6-character codes.
* **Redirection:** Accessing a short URL automatically redirects to the original long URL.
* **Basic Validation:** Ensures the input URL is not empty and starts with `http://` or `https://`.
* **Collision Handling:** Automatically retries generating a unique short code if a collision occurs.
* **User Feedback:** Provides success and error messages using Flask's flash messaging system.
* **Simple UI:** A clean and straightforward web interface for shortening URLs.
* **SQLite Database:** Stores URL mappings locally for simplicity.

## Technologies Used

* **Python:** The core programming language.
* **Flask:** A lightweight web framework for Python.
* **SQLite:** A file-based SQL database for storing URL mappings.
* **HTML/CSS:** For the user interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    *(Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install Flask
    ```

### Configuration (Optional)

You can configure the following aspects using environment variables:

* **`FLASK_SECRET_KEY`**: Essential for Flask's session management and flash messages. **Always set a strong, random key in production.**
    * Generate a key: `python -c "import os; print(os.urandom(24).hex())"`
    * **macOS/Linux:** `export FLASK_SECRET_KEY='your_generated_secret_key_here'`
    * **Windows (Command Prompt):** `set FLASK_SECRET_KEY=your_generated_secret_key_here`
    * **Windows (PowerShell):** `$env:FLASK_SECRET_KEY='your_generated_secret_key_here'`

* **`DATABASE_URL`**: Specifies the path to the SQLite database file. If not set, it defaults to `urls.db` in the project directory.
    * **macOS/Linux:** `export DATABASE_URL='/path/to/your/custom.db'`
    * **Windows (Command Prompt):** `set DATABASE_URL=C:\path\to\your\custom.db`
    * **Windows (PowerShell):** `$env:DATABASE_URL='C:\path\to\your\custom.db'`

### Running the Application

1.  **Make sure your virtual environment is active.**
2.  **Run the Flask application:**
    ```bash
    python shortenerapp.py
    ```
3.  The application will start, usually on `http://localhost:5000`. Open this URL in your web browser.

## Usage

1.  **Shorten a URL:**
    * Go to `http://localhost:5000` in your browser.
    * Enter a long URL (e.g., `https://www.google.com/search?q=url+shortener+python+flask&oq=url+shortener+python+flask`).
    * Click "Shorten URL".
    * You will see a success message with your new short URL (e.g., `http://localhost:5000/aBc1D2`).

2.  **Access a Short URL:**
    * Copy the generated short URL.
    * Paste it into your browser's address bar and press Enter.
    * You will be redirected to the original long URL.

## Project Structure
No problem! Here's a comprehensive README.md file for your URL Shortener project, tailored for GitHub. It covers everything from setup and usage to the technologies used and future improvements.

Markdown

# Simple URL Shortener

A lightweight and easy-to-use URL shortener built with Flask and SQLite. This project allows users to convert long URLs into concise, shareable short links and then redirects to the original URL when the short link is accessed.

## Features

* **URL Shortening:** Convert long, cumbersome URLs into short, random 6-character codes.
* **Redirection:** Accessing a short URL automatically redirects to the original long URL.
* **Basic Validation:** Ensures the input URL is not empty and starts with `http://` or `https://`.
* **Collision Handling:** Automatically retries generating a unique short code if a collision occurs.
* **User Feedback:** Provides success and error messages using Flask's flash messaging system.
* **Simple UI:** A clean and straightforward web interface for shortening URLs.
* **SQLite Database:** Stores URL mappings locally for simplicity.

## Technologies Used

* **Python:** The core programming language.
* **Flask:** A lightweight web framework for Python.
* **SQLite:** A file-based SQL database for storing URL mappings.
* **HTML/CSS:** For the user interface.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x installed on your system.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
    *(Replace `your-username` and `your-repo-name` with your actual GitHub username and repository name.)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows (Command Prompt):**
        ```bash
        venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install Flask
    ```

### Configuration (Optional)

You can configure the following aspects using environment variables:

* **`FLASK_SECRET_KEY`**: Essential for Flask's session management and flash messages. **Always set a strong, random key in production.**
    * Generate a key: `python -c "import os; print(os.urandom(24).hex())"`
    * **macOS/Linux:** `export FLASK_SECRET_KEY='your_generated_secret_key_here'`
    * **Windows (Command Prompt):** `set FLASK_SECRET_KEY=your_generated_secret_key_here`
    * **Windows (PowerShell):** `$env:FLASK_SECRET_KEY='your_generated_secret_key_here'`

* **`DATABASE_URL`**: Specifies the path to the SQLite database file. If not set, it defaults to `urls.db` in the project directory.
    * **macOS/Linux:** `export DATABASE_URL='/path/to/your/custom.db'`
    * **Windows (Command Prompt):** `set DATABASE_URL=C:\path\to\your\custom.db`
    * **Windows (PowerShell):** `$env:DATABASE_URL='C:\path\to\your\custom.db'`

### Running the Application

1.  **Make sure your virtual environment is active.**
2.  **Run the Flask application:**
    ```bash
    python shortenerapp.py
    ```
3.  The application will start, usually on `http://localhost:5000`. Open this URL in your web browser.

## Usage

1.  **Shorten a URL:**
    * Go to `http://localhost:5000` in your browser.
    * Enter a long URL (e.g., `https://www.google.com/search?q=url+shortener+python+flask&oq=url+shortener+python+flask`).
    * Click "Shorten URL".
    * You will see a success message with your new short URL (e.g., `http://localhost:5000/aBc1D2`).

2.  **Access a Short URL:**
    * Copy the generated short URL.
    * Paste it into your browser's address bar and press Enter.
    * You will be redirected to the original long URL.

## Project Structure

```
.
├── shortenerapp.py     # Main Flask application file
├── urls.db             # Default SQLite database file (created on first run)
└── README.md           # This file
```

## Code Overview

This section briefly explains the purpose of the main components within `shortenerapp.py`:

* **`app = Flask(__name__)`**: Initializes the core Flask application instance.
* **`app.secret_key`**: Configures the secret key crucial for securing session data and enabling flash messages.
* **`DB`**: Defines the path where the SQLite database file (`urls.db` by default) is stored.
* **`init_db()`**: A helper function executed at startup to ensure the `urls` table exists in the SQLite database, creating it if necessary.
* **`FORM_HTML`**: A multi-line string containing the complete HTML template for the main page, encompassing the URL input form and the display area for flash messages (success/error).
* **`@app.route('/', methods=['GET', 'POST'])`**: This decorator defines the behavior for the application's root URL.
    * **`GET` Request Handling**: When a user first navigates to the root URL (e.g., `http://localhost:5000/`), this part of the code renders and displays the `FORM_HTML` for URL input.
    * **`POST` Request Handling**: When the user submits the form with a long URL, this section processes the request:
        * **Input Validation**: Checks if the entered URL is valid (not empty, starts with `http://` or `https://`).
        * **Short Code Generation & Uniqueness Check**: Generates a random 6-character code and queries the database to ensure it's unique before attempting to save.
        * **Database Insertion**: Stores the `short` code and `long` URL pair into the `urls` table in the SQLite database.
        * **User Feedback**: Utilizes Flask's `flash()` mechanism to display informative success or error messages to the user.
        * **Redirection**: After processing a `POST` request, it redirects the user back to the root (`/`) to clear the form and display the flash message.
* **`@app.route('/<short>')`**: This decorator defines the behavior for accessing a shortened URL (e.g., `http://localhost:5000/xyz123`).
    * **URL Parameter Capture**: The `<short>` syntax captures the 6-character code from the URL path and passes it as an argument to the `redirect_short` function.
    * **Database Lookup**: Queries the `urls` table to find the original `long` URL associated with the captured `short` code.
    * **Redirection**: If a matching `long` URL is found in the database, the user's browser is immediately redirected to that original URL using Flask's `redirect()` function.
    * **404 Handling**: If no matching `short` URL is found, a custom "404 Not Found" HTML page is rendered and returned to the user, along with the appropriate HTTP status code.
    * **Error Handling**: Both routes include `try-except` blocks around database operations to gracefully handle potential `sqlite3.Error` exceptions and provide user-friendly error messages or log internal errors.
* **`if __name__ == '__main__':`**: This standard Python construct ensures that the `init_db()` function is called (to set up the database) and the Flask development server (`app.run(debug=True)`) starts only when the `shortenerapp.py` script is executed directly, not when it's imported as a module into another script.

## Future Improvements

* **Custom Short URLs:** Allow users to specify their desired short code instead of just random ones.
* **Analytics:** Track the number of clicks for each short URL.
* **User Accounts:** Implement user registration and login to manage personal short URLs.
* **Expiration Dates:** Allow setting an expiration date for short URLs.
* **Error Logging:** Implement more sophisticated logging (e.g., to a file) instead of just printing to console.
* **Dockerization:** Package the application in a Docker container for easier deployment.
* **Frontend Framework:** Use a JavaScript framework (e.g., React, Vue) for a more interactive UI.
* **Deployment:** Instructions for deploying to platforms like Heroku, Render, Vercel, etc.
* **Rate Limiting:** Implement a mechanism to prevent abuse (e.g., too many shorten requests from one IP).
* **Advanced Validation:** Use a more robust URL validation library.

## Contributing

Feel free to fork the repository, open issues, and submit pull requests.

## License

This project is open source and available under the [MIT License](LICENSE). *(You'll need to create a LICENSE file if you haven't already).*
