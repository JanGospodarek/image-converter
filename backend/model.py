from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class ImageModel(db.Model):
    name=db.Column(db.String(100),nullable=False,primary_key=True)
    def __repr__(self):
        return  f'Image(name={self.name})'

