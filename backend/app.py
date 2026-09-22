from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from backend.config import Config
from backend.database import db
from backend.models.user import User
from backend.routes.auth import auth_bp
from backend.routes.customer import customer_bp
from backend.routes.entrepreneur import entrepreneur_bp
from backend.routes.admin import admin_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

CORS(
    app,
    supports_credentials=True,
    origins=["http://127.0.0.1:5500"]
)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(entrepreneur_bp)
app.register_blueprint(admin_bp)

@app.route("/")
def home():
    return {
        "message": "HunarHub API is running",
        "status": "success"
    }

if __name__ == "__main__":
    app.run(debug=True)
