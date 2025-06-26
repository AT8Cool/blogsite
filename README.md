📝 BlogSite

A simple and functional blog web application built using Flask, SQLAlchemy, and WTForms. It allows users to register, log in, and create, view, and manage blog posts in a clean and user-friendly interface.

🚀 Features

🔐 User Authentication (Register/Login/Logout)

🖋️ Create, Edit, and Delete Blog Posts

📜 View All Posts with Timestamps

🧠 Form Validation using Flask-WTF

📁 MySQL Integration with SQLAlchemy ORM

🧼 Clean UI with Jinja2 Templates


🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, Bootstrap, Jinja2

Database: MySQL

ORM: SQLAlchemy

Forms: Flask-WTF


📁 Folder Structure

blogsite/
│
├── static/              # CSS, JS, and images
├── templates/           # HTML templates (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
├── app.py               # Main Flask application
├── models.py            # Database models
├── forms.py             # WTForms for login/register
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

🔧 Setup Instructions

1. Clone the repo:



git clone https://github.com/AT8Cool/blogsite.git
cd blogsite

2. Create and activate a virtual environment:



python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies:



pip install -r requirements.txt

4. Configure your MySQL database:



Update the app.config['SQLALCHEMY_DATABASE_URI'] in app.py:

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'

5. Run the app:



python app.py

Visit http://127.0.0.1:5000 in your browser.

📸 Screenshots

(Will Update in the next commit)

📚 Things I would want to add

Add support for image uploads

Markdown support for posts

Password encryption with hashing

Pagination for posts


🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

📄 License

This project is licensed under the MIT License.


---

Let me know if you'd like to add deployment instructions (e.g., on Heroku or Render) or a requirements.txt file generator.

