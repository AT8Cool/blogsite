# 📝 BlogSite

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?logo=flask)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A minimalistic blog application built with **Flask**, **MySQL**, and **WTForms**. Users can register, log in, and publish blog posts with ease.

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
| Frontend  | HTML5, CSS3              |
| Forms     | Flask-WTF, WTForms       |
| Database  | MySQL                    |

---

## 📁 Project Structure

```bash
blogsite/
├── static/                  # CSS, JS, and images
├── templates/               # HTML templates (Jinja2)
│   ├── create_post.html
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│ 
├── app.py                   # Main Flask applicationms for login/register
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```
---

## 🛠️ Setup Instructions

## 🔗 Clone the Repo

```
git clone https://github.com/AT8Cool/blogsite.git
cd blogsite
```
---
## 💻 Create and Activate Virtual Environment
```
bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```
---
## 📦 Install Dependencies
```
pip install -r requirements.txt
```
---
## ⚙️ Configure MySQL Database
  ### Edit this line in app.py:
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
```
---
## ▶️ Run the App
```
python app.py
```
Then visit http://127.0.0.1:7777 in your browser.
