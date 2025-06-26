
📝 BlogSite

A simple and clean blogging platform built with Flask, MySQL, and WTForms. Users can sign up, log in, create blog posts, and view them in reverse chronological order.


---

📌 Features

🔐 User authentication (signup/login/logout)

📝 Create and publish blog posts

🗂️ View all blog entries on the homepage

✅ Form validation using Flask-WTF

💾 Data handling via SQLAlchemy ORM with MySQL



---

📁 Folder Structure

blogsite/
├── static/                   # Static files (CSS, JS, images)
├── templates/                # HTML templates
│   ├── create_post.html
│   ├── index.html
│   ├── login.html
│   └── signup.html
├── app.py                    # Main Flask application
├── tempCodeRunnerFile.py     # Temporary file (can be ignored/deleted)
├── .gitignore
└── README.md                 # Project documentation


---

⚙️ Installation & Setup

1. Clone the Repository

git clone https://github.com/AT8Cool/blogsite.git
cd blogsite

2. Create and Activate a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

3. Install Dependencies

Make sure pip is updated:

pip install -r requirements.txt

If requirements.txt is missing, you can create it:

Flask
Flask-WTF
Flask-SQLAlchemy
pymysql
wtforms

4. Setup MySQL Database

1. Make sure MySQL is installed and running.


2. Log into your MySQL terminal and create a database:



CREATE DATABASE blogsite;

3. Update the DB URI in app.py:



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:<yourpassword>@localhost/blogsite'


---

🧪 Running the App

python app.py

Then visit 👉 http://localhost:7777


---

✨ Pages Overview

Route	Description

/	Homepage showing all blog posts
/login	Login page
/signup	Signup page
/logout	Logs the user out
/blog_posting	Form for writing a new blog
/new	Handles post submission


