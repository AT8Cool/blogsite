class User_data(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(150),nullable=False,unique=True)
    password = db.Column(db.String(900),nullable = False)