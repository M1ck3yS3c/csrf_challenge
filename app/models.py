from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    #Creating uer table

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30),  unique=True, nullable=False)
    password_hash = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean, default=False)


    @property

    def password(self):


        #prevent password from being accessed

        raise AttributeError('Password is not a readable attribute.')

    @password.setter

    def password(self, password):

        #set password to a hashed password

        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        #check if hash matches actual password
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)


#setup user loader
@login_manager.user_loader

def load_user(user_id):
    return User.query.get(int(user_id))

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60),nullable=False)
    body = db.Column(db.String(400))
    author = db.Column(db.String(30), db.ForeignKey('users.username'))
    response = db.Column(db.String(60))
    def __repr__(self):
        return '<Message: {}>'.format(self.author)


