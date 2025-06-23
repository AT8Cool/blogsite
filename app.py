from flask import Flask,render_template,request,redirect, session,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired


app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')

#Configure MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yourpassword@localhost/blogsite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#WTForms secret key
app.config['SECRET_KEY']= 'hello'
#Initializa the DB object
db = SQLAlchemy(app)

#Define BlogPost
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)

#Login
class User_data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150),nullable=False,unique=True)
    password = db.Column(db.String(8),nullable = False)

#Create a Form Class
class LoginForm(FlaskForm):
    username = StringField("What's your name",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Submit")


#Create the tables
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    posts = BlogPost.query.all()
    posts = posts[::-1]
    return render_template("index.html", posts=posts)


@app.route('/blog_posting',methods=['POST'])
def create_post():
    return render_template("create_post.html")


@app.route('/new',methods=['POST'])
def add_new_post():
    title = request.form.get('title-area')
    content = request.form.get('Content')
    author = 'Anoymous'
    if title and content:
        new_post = BlogPost(title=title,content=content,author=author)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('index'))
   
#Create login page
@app.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    #Validate
    if form.validate_on_submit():
        username = form.username.data
        user = User_data.query.filter_by(username=username).first()
        if user:
            session['username'] = user.username 
            return redirect(url_for('index'))
        else:
            return "<h1>User not found</h1>",401

    return render_template('login.html',form = form)


#Signup page
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method =='POST':
       
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            existing_user = User_data.query.filter_by(username=username).first()
           
            if  existing_user:
                return "User name already exist",409
            
            new_user = User_data(username=username,password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/logout',methods=['GET'])
def logout():
        session.pop('username',None)
        return redirect(url_for('index'))

if '__main__' == __name__:
    app.run(debug=True,port=7777)