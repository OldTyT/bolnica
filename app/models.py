from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ward = db.Column(db.String(), index=True)
    bed = db.Column(db.String(), index=True)
    date = db.Column(db.String(), index=True)
    coment = db.Column(db.String(), index=True)

    def __repr__(self):
        return f'<Patient {self.ward}-{self.bed}>'