from backend.database import db

class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    entrepreneur_id = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    estimated_time = db.Column(db.String(100))
    availability = db.Column(db.Boolean, default=True)
    status = db.Column(db.Enum("ACTIVE", "INACTIVE"), default="ACTIVE")
