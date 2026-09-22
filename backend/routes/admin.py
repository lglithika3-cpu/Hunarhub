from flask import Blueprint, jsonify, request
from flask_login import current_user
from backend.database import db
from backend.security.roles import role_required
from backend.models.user import User
from backend.models.category import Category
from backend.models.product import Product
from backend.models.service import Service
from backend.models.order import Order
from backend.models.review import Review
from backend.models.service_request import ServiceRequest
from backend.models.entrepreneur import Entrepreneur

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/dashboard", methods=["GET"])
@role_required("ADMIN")
def dashboard():
    return jsonify({
        "message": "Admin dashboard",
        "users": db.session.execute(db.select(User)).scalars().all().__len__(),
        "products": db.session.execute(db.select(Product)).scalars().all().__len__(),
        "orders": db.session.execute(db.select(Order)).scalars().all().__len__(),
        "reviews": db.session.execute(db.select(Review)).scalars().all().__len__()
    })

@admin_bp.route("/users", methods=["GET"])
@role_required("ADMIN")
def users():
    users = db.session.execute(db.select(User)).scalars().all()

    return jsonify([{
        "id": u.id,
        "name": u.name,
        "email": u.email,
        "role": u.role,
        "created_at": str(u.created_at)
    } for u in users])

@admin_bp.route("/users/<int:user_id>/role", methods=["PUT", "PATCH"])
@role_required("ADMIN")
def update_user_role(user_id):
    user = db.session.get(User, user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json() or {}
    role = str(data.get("role", "")).upper()

    if role not in ["CUSTOMER", "ENTREPRENEUR", "ADMIN"]:
        return jsonify({"error": "Invalid role"}), 400

    user.role = role
    db.session.commit()

    return jsonify({
        "message": "User role updated",
        "id": user.id,
        "role": user.role
    })

@admin_bp.route("/categories", methods=["GET", "POST"])
@role_required("ADMIN")
def categories():
    if request.method == "GET":
        categories = db.session.execute(
            db.select(Category)
        ).scalars().all()

        return jsonify([{
            "id": c.id,
            "name": c.name,
            "description": c.description,
            "status": c.status
        } for c in categories])

    data = request.get_json() or {}

    if not data.get("name"):
        return jsonify({"error": "Category name is required"}), 400

    category = Category(
        name=data["name"],
        description=data.get("description"),
        status=data.get("status", "ACTIVE")
    )

    db.session.add(category)
    db.session.commit()

    return jsonify({
        "message": "Category created",
        "id": category.id
    }), 201

@admin_bp.route("/categories/<int:category_id>", methods=["PUT", "DELETE"])
@role_required("ADMIN")
def category_manage(category_id):
    category = db.session.get(Category, category_id)

    if not category:
        return jsonify({"error": "Category not found"}), 404

    if request.method == "DELETE":
        category.status = "INACTIVE"
        db.session.commit()
        return jsonify({"message": "Category deactivated"})

    data = request.get_json() or {}

    if "name" in data:
        category.name = data["name"]
    if "description" in data:
        category.description = data["description"]
    if "status" in data:
        category.status = data["status"]

    db.session.commit()

    return jsonify({"message": "Category updated"})

@admin_bp.route("/products", methods=["GET"])
@role_required("ADMIN")
def products():
    products = db.session.execute(db.select(Product)).scalars().all()

    return jsonify([{
        "id": p.id,
        "entrepreneur_id": p.entrepreneur_id,
        "category_id": p.category_id,
        "name": p.name,
        "description": p.description,
        "price": float(p.price),
        "stock": p.stock,
        "image_url": p.image_url,
        "status": p.status
    } for p in products])

@admin_bp.route("/services", methods=["GET"])
@role_required("ADMIN")
def services():
    services = db.session.execute(db.select(Service)).scalars().all()

    return jsonify([{
        "id": s.id,
        "entrepreneur_id": s.entrepreneur_id,
        "category_id": s.category_id,
        "name": s.name,
        "description": s.description,
        "price": float(s.price),
        "estimated_time": s.estimated_time,
        "availability": s.availability,
        "status": s.status
    } for s in services])

@admin_bp.route("/orders", methods=["GET"])
@role_required("ADMIN")
def orders():
    orders = db.session.execute(db.select(Order)).scalars().all()

    return jsonify([{
        "id": o.id,
        "customer_id": o.customer_id,
        "entrepreneur_id": o.entrepreneur_id,
        "total_amount": float(o.total_amount),
        "status": o.status,
        "created_at": str(o.created_at)
    } for o in orders])

@admin_bp.route("/reviews", methods=["GET"])
@role_required("ADMIN")
def reviews():
    reviews = db.session.execute(db.select(Review)).scalars().all()

    return jsonify([{
        "id": r.id,
        "customer_id": r.customer_id,
        "entrepreneur_id": r.entrepreneur_id,
        "product_id": r.product_id,
        "rating": r.rating,
        "review_text": r.review_text,
        "created_at": str(r.created_at)
    } for r in reviews])

@admin_bp.route("/service-requests", methods=["GET"])
@role_required("ADMIN")
def service_requests():
    requests = db.session.execute(
        db.select(ServiceRequest)
    ).scalars().all()

    return jsonify([{
        "id": r.id,
        "customer_id": r.customer_id,
        "entrepreneur_id": r.entrepreneur_id,
        "service_id": r.service_id,
        "request_description": r.request_description,
        "preferred_date": str(r.preferred_date) if r.preferred_date else None,
        "status": r.status
    } for r in requests])

@admin_bp.route("/entrepreneurs", methods=["GET"])
@role_required("ADMIN")
def entrepreneurs():
    entrepreneurs = db.session.execute(
        db.select(Entrepreneur)
    ).scalars().all()

    return jsonify([{
        "id": e.id,
        "user_id": e.user_id,
        "business_name": e.business_name,
        "verification_status": e.verification_status,
        "availability_status": e.availability_status
    } for e in entrepreneurs])

@admin_bp.route("/reports", methods=["GET"])
@role_required("ADMIN")
def reports():
    users = db.session.execute(db.select(User)).scalars().all()
    products = db.session.execute(db.select(Product)).scalars().all()
    orders = db.session.execute(db.select(Order)).scalars().all()
    services = db.session.execute(db.select(Service)).scalars().all()
    reviews = db.session.execute(db.select(Review)).scalars().all()

    completed_orders = [
        o for o in orders if o.status == "COMPLETED"
    ]

    revenue = sum(float(o.total_amount) for o in completed_orders)

    return jsonify({
        "total_users": len(users),
        "total_products": len(products),
        "total_services": len(services),
        "total_orders": len(orders),
        "completed_orders": len(completed_orders),
        "total_reviews": len(reviews),
        "total_revenue": revenue
    })

@admin_bp.route("/profile", methods=["GET"])
@role_required("ADMIN")
def profile():
    return jsonify({
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role
    })
