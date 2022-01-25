from app import db
from datetime import datetime


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ward = db.Column(db.String(), index=True)
    bed = db.Column(db.String(), index=True)
    datetime = db.Column(db.DateTime(), default=datetime.now, index=True)
    comment = db.Column(db.String(), index=True)
    active = db.Column(db.Boolean, default=True, index=True)

    def __repr__(self):
        return f'<Patient Ward - {self.ward}. Bed - {self.bed}>'
