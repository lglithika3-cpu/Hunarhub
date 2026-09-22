from datetime import datetime
from backend.database import db

class Entrepreneur(db.Model):
    __tablename__ = "entrepreneurs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    business_name = db.Column(db.String(150), nullable=False)
    bio = db.Column(db.Text)
    skill_description = db.Column(db.Text)
    experience = db.Column(db.String(100))
    address_area = db.Column(db.String(150))
    latitude = db.Column(db.Numeric(10, 8))
    longitude = db.Column(db.Numeric(11, 8))
    location_visibility = db.Column(
        db.Enum("EXACT", "AREA_ONLY", "HIDDEN"),
        default="AREA_ONLY"
    )
    verification_status = db.Column(
        db.Enum("PENDING", "VERIFIED", "REJECTED"),
        default="PENDING"
    )
    availability_status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)