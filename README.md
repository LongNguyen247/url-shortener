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

.
├── shortenerapp.py     # Main Flask application file
├── urls.db             # Default SQLite database file (created on first run)
└── README.md           # This file
