# 🔗 Simple URL Shortener

A lightweight and modular **URL Shortener** built with **Flask** and **SQLite**.  
This project allows users to convert long URLs into concise, shareable short links and automatically redirects users when they visit the shortened link.

---

## ✨ Features

- **URL Shortening:** Convert long URLs into short, random 6-character codes.  
- **Redirection:** Visiting a short URL redirects to the original long URL.  
- **Validation:** Ensures the input starts with `http://` or `https://`.  
- **User Feedback:** Success and error messages displayed via Flask's flash system.  
- **SQLite Database:** Stores mappings between short and long URLs.  
- **Custom Error Page:** Graceful 404 page if a short URL does not exist.  
- **Clean UI:** Simple HTML templates with optional CSS styling.  
- **Modular Codebase:** Logic is split into multiple files (`app.py`, `db.py`, `utils.py`) for clarity and maintainability.  

---

## 🛠️ Technologies Used

- **Python 3** — core programming language  
- **Flask** — web framework  
- **SQLite** — lightweight file-based database  
- **Jinja2 Templates (HTML)** — frontend pages  
- **CSS** — optional styling  

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
