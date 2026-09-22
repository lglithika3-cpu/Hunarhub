from datetime import datetime
from backend.database import db

class ServiceRequest(db.Model):
    __tablename__ = "service_requests"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, nullable=False)
    entrepreneur_id = db.Column(db.Integer, nullable=False)
    service_id = db.Column(db.Integer, nullable=False)
    request_description = db.Column(db.Text)
    preferred_date = db.Column(db.Date)
    status = db.Column(
        db.Enum("PENDING", "ACCEPTED", "REJECTED", "COMPLETED", "CANCELLED"),
        default="PENDING"
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )