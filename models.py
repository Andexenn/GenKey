from app import db

class User(db.Model):
    __tablename__ = "user"
    
    username = db.Column(db.Text, nullable=False, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"User with name: {self.username} and passowrd: {self.password}"
    