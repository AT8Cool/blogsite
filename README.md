

```
# 📝 BlogSite

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A minimalistic blog application built with **Flask**, **MySQL**, and **WTForms**. Users can register, log in, and publish blog posts with ease.

---

## 📸 Screenshots

| Home Page | Login | Dashboard |
|----------|-------|-----------|
| ![Home](static/screenshots/home.png) | ![Login](static/screenshots/login.png) | ![Dashboard](static/screenshots/dashboard.png) |

---

## ⚙️ Features

- 🔐 User Authentication (Register/Login/Logout)
- 🖋️ Create, Edit, and Delete Posts
- 🧼 Form Validation (Flask-WTF)
- 📁 MySQL Integration via SQLAlchemy
- 🧩 Modular Template Structure with Jinja2

---

## 🛠️ Tech Stack

| Layer     | Technology              |
|-----------|--------------------------|
| Backend   | Flask, SQLAlchemy        |
| Frontend  | HTML5, CSS3, Bootstrap   |
| Forms     | Flask-WTF, WTForms       |
| Database  | MySQL                    |

---

## 🗂️ Project Structure

```

blogsite/
│
├── static/              # CSS, JS, images
├── templates/           # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── app.py               # Main Flask app
├── models.py            # SQLAlchemy models
├── forms.py             # WTForms classes
├── requirements.txt     # Python dependencies
└── README.md            # This file

````

---

## 🚀 Setup & Run Locally

### 🔧 Prerequisites

- Python 3.8+
- MySQL
- Virtualenv (optional but recommended)

### 💻 Installation

```bash
# Clone the repository
git clone https://github.com/AT8Cool/blogsite.git
cd blogsite

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
````

### 🛠️ Configure Database

Edit `app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
```

### ▶️ Run the App

```bash
python app.py
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📌 To-Do / Roadmap

* [ ] Add Markdown support for blog posts
* [ ] Improve UI with a theme or dark mode
* [ ] Add profile pictures and user bios
* [ ] Add search and pagination
* [ ] Hash passwords with `werkzeug.security`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Have suggestions or improvements? Feel free to:

* Fork the repo
* Create a new branch
* Submit a pull request

---

## 💬 Contact

**Atharva Bhosale**
📧 [at8cool@gmail.com](mailto:at8cool@gmail.com)
🌐 [GitHub](https://github.com/AT8Cool)

---

```

---
Updated README with detailed markdown layout
