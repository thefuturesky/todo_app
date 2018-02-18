from exts import db
from datetime import datetime

class Todo(db.Model):
    __tablename__='todo'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    content=db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    status=db.Column(db.Integer,default=0)