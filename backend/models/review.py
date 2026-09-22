from datetime import datetime
from backend.database import db

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    entrepreneur_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.Integer, nullable=False)
    review_text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)