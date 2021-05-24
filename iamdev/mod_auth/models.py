from iamdev import db

class Base(db.Model):
    __abstract__    = True
    id              = db.Column(db.Integer, primary_key=True)
    date_created    = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified   = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                onupdate=db.func.current_timestamp())
    

class User(Base):
    __tablename__   = 'auth_user'
    
    # user data base
    name            = db.Column(db.String(128), nullable=False)
    email           = db.Column(db.String(128), nullable=False)
    password        = db.Column(db.String(192), nullable=False)
    
    # Auth roles
    role            = db.Column(db.SmallInteger, nullable=False)
    status          = db.Column(db.SmallInteger, nullable=False)
    
    # new instance
    def __init__(self, name, email, passowrd):
        
        self.name   = name
        self.email  = email
        self.password = password
        
    def __repr__(self):
        return '<User %r>' % (self.name)