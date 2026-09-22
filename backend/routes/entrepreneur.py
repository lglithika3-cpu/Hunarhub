from flask import Blueprint, jsonify, request
from flask_login import current_user
from backend.database import db
from backend.security.roles import role_required
from backend.models.product import Product
from backend.models.category import Category
from backend.models.entrepreneur import Entrepreneur
from backend.models.order import Order
from backend.models.order_item import OrderItem
from backend.models.service import Service
from backend.models.service_request import ServiceRequest

entrepreneur_bp = Blueprint("entrepreneur", __name__, url_prefix="/entrepreneur")

def get_profile():
    return db.session.execute(
        db.select(Entrepreneur).where(
            Entrepreneur.user_id == current_user.id
        )
    ).scalar_one_or_none()

@entrepreneur_bp.route("/dashboard", methods=["GET"])
@role_required("ENTREPRENEUR")
def dashboard():
    entrepreneur = get_profile()

    if not entrepreneur:
        return jsonify({"message": "Entrepreneur profile not created yet"})

    products = db.session.execute(
        db.select(Product).where(Product.entrepreneur_id == entrepreneur.id)
    ).scalars().all()

    orders = db.session.execute(
        db.select(Order).where(Order.entrepreneur_id == entrepreneur.id)
    ).scalars().all()

    return jsonify({
        "message": "Entrepreneur dashboard",
        "business_name": entrepreneur.business_name,
        "product_count": len(products),
        "order_count": len(orders),
        "verification_status": entrepreneur.verification_status
    })

@entrepreneur_bp.route("/profile", methods=["GET", "PUT"])
@role_required("ENTREPRENEUR")
def profile():
    entrepreneur = get_profile()

    if request.method == "PUT":
        data = request.get_json() or {}

        if not entrepreneur:
            if not data.get("business_name"):
                return jsonify({"error": "business_name is required"}), 400

            entrepreneur = Entrepreneur(
                user_id=current_user.id,
                business_name=data["business_name"]
            )
            db.session.add(entrepreneur)

        for field in [
            "business_name",
            "bio",
            "skill_description",
            "experience",
            "address_area",
            "latitude",
            "longitude",
            "location_visibility",
            "availability_status"
        ]:
            if field in data:
                setattr(entrepreneur, field, data[field])

        db.session.commit()

    if not entrepreneur:
        return jsonify({"message": "Entrepreneur profile not created"})

    return jsonify({
        "id": entrepreneur.id,
        "user_id": entrepreneur.user_id,
        "business_name": entrepreneur.business_name,
        "bio": entrepreneur.bio,
        "skill_description": entrepreneur.skill_description,
        "experience": entrepreneur.experience,
        "address_area": entrepreneur.address_area,
        "latitude": str(entrepreneur.latitude) if entrepreneur.latitude else None,
        "longitude": str(entrepreneur.longitude) if entrepreneur.longitude else None,
        "location_visibility": entrepreneur.location_visibility,
        "verification_status": entrepreneur.verification_status,
        "availability_status": entrepreneur.availability_status
    })

@entrepreneur_bp.route("/products", methods=["GET", "POST"])
@role_required("ENTREPRENEUR")
def products():
    entrepreneur = get_profile()

    if not entrepreneur:
        return jsonify({"error": "Create entrepreneur profile first"}), 400

    if request.method == "GET":
        products = db.session.execute(
            db.select(Product).where(
                Product.entrepreneur_id == entrepreneur.id
            )
        ).scalars().all()

        return jsonify([{
            "id": p.id,
            "category_id": p.category_id,
            "name": p.name,
            "description": p.description,
            "price": float(p.price),
            "stock": p.stock,
            "image_url": p.image_url,
            "status": p.status
        } for p in products])

    data = request.get_json() or {}

    required = ["category_id", "name", "price"]

    if any(data.get(x) is None for x in required):
        return jsonify({"error": "category_id, name and price are required"}), 400

    product = Product(
        entrepreneur_id=entrepreneur.id,
        category_id=data["category_id"],
        name=data["name"],
        description=data.get("description"),
        price=data["price"],
        stock=data.get("stock", 0),
        image_url=data.get("image_url"),
        status=data.get("status", "ACTIVE")
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product created successfully",
        "id": product.id
    }), 201

@entrepreneur_bp.route("/products/<int:product_id>", methods=["PUT", "DELETE"])
@role_required("ENTREPRENEUR")
def product_manage(product_id):
    entrepreneur = get_profile()
    product = db.session.get(Product, product_id)

    if not product or not entrepreneur or product.entrepreneur_id != entrepreneur.id:
        return jsonify({"error": "Product not found"}), 404

    if request.method == "DELETE":
        product.status = "INACTIVE"
        db.session.commit()
        return jsonify({"message": "Product deactivated"})

    data = request.get_json() or {}

    for field in [
        "category_id",
        "name",
        "description",
        "price",
        "stock",
        "image_url",
        "status"
    ]:
        if field in data:
            setattr(product, field, data[field])

    db.session.commit()

    return jsonify({"message": "Product updated successfully"})

@entrepreneur_bp.route("/services", methods=["GET", "POST"])
@role_required("ENTREPRENEUR")
def services():
    entrepreneur = get_profile()

    if not entrepreneur:
        return jsonify({"error": "Create entrepreneur profile first"}), 400

    if request.method == "GET":
        services = db.session.execute(
            db.select(Service).where(
                Service.entrepreneur_id == entrepreneur.id
            )
        ).scalars().all()

        return jsonify([{
            "id": s.id,
            "category_id": s.category_id,
            "name": s.name,
            "description": s.description,
            "price": float(s.price),
            "estimated_time": s.estimated_time,
            "availability": s.availability,
            "status": s.status
        } for s in services])

    data = request.get_json() or {}

    service = Service(
        entrepreneur_id=entrepreneur.id,
        category_id=data.get("category_id"),
        name=data.get("name"),
        description=data.get("description"),
        price=data.get("price", 0),
        estimated_time=data.get("estimated_time"),
        availability=data.get("availability", True),
        status=data.get("status", "ACTIVE")
    )

    db.session.add(service)
    db.session.commit()

    return jsonify({
        "message": "Service created successfully",
        "id": service.id
    }), 201

@entrepreneur_bp.route("/services/<int:service_id>", methods=["PUT", "DELETE"])
@role_required("ENTREPRENEUR")
def service_manage(service_id):
    entrepreneur = get_profile()
    service = db.session.get(Service, service_id)

    if not service or not entrepreneur or service.entrepreneur_id != entrepreneur.id:
        return jsonify({"error": "Service not found"}), 404

    if request.method == "DELETE":
        service.status = "INACTIVE"
        db.session.commit()
        return jsonify({"message": "Service deactivated"})

    data = request.get_json() or {}

    for field in [
        "category_id",
        "name",
        "description",
        "price",
        "estimated_time",
        "availability",
        "status"
    ]:
        if field in data:
            setattr(service, field, data[field])

    db.session.commit()

    return jsonify({"message": "Service updated successfully"})

@entrepreneur_bp.route("/orders", methods=["GET"])
@role_required("ENTREPRENEUR")
def orders():
    entrepreneur = get_profile()

    if not entrepreneur:
        return jsonify([])

    orders = db.session.execute(
        db.select(Order).where(
            Order.entrepreneur_id == entrepreneur.id
        )
    ).scalars().all()

    return jsonify([{
        "id": o.id,
        "customer_id": o.customer_id,
        "total_amount": float(o.total_amount),
        "status": o.status,
        "created_at": str(o.created_at)
    } for o in orders])

@entrepreneur_bp.route("/orders/<int:order_id>", methods=["PUT"])
@role_required("ENTREPRENEUR")
def update_order(order_id):
    entrepreneur = get_profile()
    order = db.session.get(Order, order_id)

    if not order or not entrepreneur or order.entrepreneur_id != entrepreneur.id:
        return jsonify({"error": "Order not found"}), 404

    data = request.get_json() or {}
    status = data.get("status")

    allowed = ["PENDING", "CONFIRMED", "COMPLETED", "CANCELLED"]

    if status not in allowed:
        return jsonify({"error": "Invalid order status"}), 400

    order.status = status
    db.session.commit()

    return jsonify({"message": "Order status updated"})

@entrepreneur_bp.route("/service-requests", methods=["GET", "PUT"])
@role_required("ENTREPRENEUR")
def service_requests():
    entrepreneur = get_profile()

    if not entrepreneur:
        return jsonify([])

    if request.method == "GET":
        requests = db.session.execute(
            db.select(ServiceRequest).where(
                ServiceRequest.entrepreneur_id == entrepreneur.id
            )
        ).scalars().all()

        return jsonify([{
            "id": r.id,
            "customer_id": r.customer_id,
            "service_id": r.service_id,
            "request_description": r.request_description,
            "preferred_date": str(r.preferred_date) if r.preferred_date else None,
            "status": r.status
        } for r in requests])

    data = request.get_json() or {}
    request_id = data.get("id")
    new_status = data.get("status")

    service_request = db.session.get(ServiceRequest, request_id)

    if not service_request or service_request.entrepreneur_id != entrepreneur.id:
        return jsonify({"error": "Service request not found"}), 404

    if new_status not in [
        "PENDING",
        "ACCEPTED",
        "REJECTED",
        "COMPLETED",
        "CANCELLED"
    ]:
        return jsonify({"error": "Invalid status"}), 400

    service_request.status = new_status
    db.session.commit()

    return jsonify({"message": "Service request updated"})

@entrepreneur_bp.route("/earnings", methods=["GET"])
@role_required("ENTREPRENEUR")
def earnings():
    entrepreneur = get_profile()

    if not entrepreneur:
        return jsonify({"total_earnings": 0})

    orders = db.session.execute(
        db.select(Order).where(
            Order.entrepreneur_id == entrepreneur.id,
            Order.status == "COMPLETED"
        )
    ).scalars().all()

    total = sum(float(o.total_amount) for o in orders)

    return jsonify({
        "total_earnings": total,
        "completed_orders": len(orders)
    })
