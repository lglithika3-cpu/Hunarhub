from flask import Blueprint, jsonify, request
from flask_login import current_user
from backend.database import db
from backend.security.roles import role_required
from backend.models.user import User
from backend.models.product import Product
from backend.models.service import Service
from backend.models.order import Order
from backend.models.order_item import OrderItem
from backend.models.service_request import ServiceRequest
from backend.models.review import Review

customer_bp = Blueprint("customer", __name__, url_prefix="/api/customer")

@customer_bp.get("/profile")
@role_required("CUSTOMER")
def profile():
    user = db.session.get(User, current_user.id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "role": user.role
    }), 200

@customer_bp.get("/products")
@role_required("CUSTOMER")
def products():
    products = Product.query.all()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "price": float(p.price) if p.price is not None else 0,
            "category_id": p.category_id,
            "entrepreneur_id": p.entrepreneur_id,
            "stock": p.stock,
            "status": p.status
        }
        for p in products
    ]), 200

@customer_bp.get("/services")
@role_required("CUSTOMER")
def services():
    services = Service.query.all()
    return jsonify([
        {
            "id": s.id,
            "name": s.name,
            "description": s.description,
            "price": float(s.price) if s.price is not None else 0,
            "entrepreneur_id": s.entrepreneur_id
        }
        for s in services
    ]), 200

@customer_bp.get("/orders")
@role_required("CUSTOMER")
def orders():
    orders = Order.query.filter_by(customer_id=current_user.id).all()
    return jsonify([
        {
            "id": o.id,
            "customer_id": o.customer_id,
            "entrepreneur_id": o.entrepreneur_id,
            "status": o.status,
            "total_amount": float(o.total_amount) if o.total_amount is not None else 0,
            "created_at": o.created_at.isoformat() if o.created_at else None
        }
        for o in orders
    ]), 200

@customer_bp.post("/orders")
@role_required("CUSTOMER")
def create_order():
    data = request.get_json() or {}
    items = data.get("items", [])

    if not isinstance(items, list) or not items:
        return jsonify({
            "error": "Order items are required"
        }), 400

    total = 0
    entrepreneur_id = None
    order_items_data = []

    try:
        for item in items:
            product_id = item.get("product_id")
            quantity_value = item.get("quantity", 1)

            try:
                quantity = int(quantity_value)
            except (TypeError, ValueError):
                return jsonify({
                    "error": "Quantity must be a number"
                }), 400

            if not product_id or quantity <= 0:
                return jsonify({
                    "error": "Invalid order item"
                }), 400

            product = Product.query.get(product_id)

            if not product:
                return jsonify({
                    "error": f"Product {product_id} not found"
                }), 404

            if entrepreneur_id is None:
                entrepreneur_id = product.entrepreneur_id
            elif int(product.entrepreneur_id) != int(entrepreneur_id):
                return jsonify({
                    "error": "All products in one order must belong to the same entrepreneur"
                }), 400

            price = float(product.price) if product.price is not None else 0
            subtotal = price * quantity
            total += subtotal

            order_items_data.append({
                "product_id": product.id,
                "quantity": quantity,
                "price": price
            })

        if entrepreneur_id is None:
            return jsonify({
                "error": "Unable to determine entrepreneur"
            }), 400

        order = Order(
            customer_id=current_user.id,
            entrepreneur_id=entrepreneur_id,
            status="PENDING",
            total_amount=total
        )

        db.session.add(order)
        db.session.flush()

        for item in order_items_data:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item["product_id"],
                quantity=item["quantity"],
                price=item["price"]
            )
            db.session.add(order_item)

        db.session.commit()

    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "Unable to create order"
        }), 500

    return jsonify({
        "message": "Order created successfully",
        "order_id": order.id,
        "entrepreneur_id": entrepreneur_id,
        "total_amount": total
    }), 201

@customer_bp.get("/service-requests")
@role_required("CUSTOMER")
def service_requests():
    requests = ServiceRequest.query.filter_by(
        customer_id=current_user.id
    ).all()

    return jsonify([
        {
            "id": r.id,
            "entrepreneur_id": r.entrepreneur_id,
            "service_id": r.service_id,
            "request_description": r.request_description,
            "preferred_date": r.preferred_date.isoformat() if r.preferred_date else None,
            "status": r.status,
            "created_at": r.created_at.isoformat() if r.created_at else None
        }
        for r in requests
    ]), 200

@customer_bp.post("/service-requests")
@role_required("CUSTOMER")
def create_service_request():
    data = request.get_json() or {}

    entrepreneur_id = data.get("entrepreneur_id")
    service_id = data.get("service_id")
    description = data.get("request_description")
    preferred_date = data.get("preferred_date")

    if not entrepreneur_id or not service_id or not description:
        return jsonify({
            "error": "entrepreneur_id, service_id and request_description are required"
        }), 400

    service = Service.query.get(service_id)

    if not service:
        return jsonify({
            "error": "Service not found"
        }), 404

    if int(service.entrepreneur_id) != int(entrepreneur_id):
        return jsonify({
            "error": "Service does not belong to the selected entrepreneur"
        }), 400

    request_record = ServiceRequest(
        customer_id=current_user.id,
        entrepreneur_id=entrepreneur_id,
        service_id=service_id,
        request_description=description,
        preferred_date=preferred_date,
        status="PENDING"
    )

    try:
        db.session.add(request_record)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "Unable to create service request"
        }), 500

    return jsonify({
        "message": "Service request created successfully",
        "request_id": request_record.id
    }), 201

@customer_bp.get("/reviews")
@role_required("CUSTOMER")
def reviews():
    reviews = Review.query.filter_by(
        customer_id=current_user.id
    ).all()

    return jsonify([
        {
            "id": r.id,
            "product_id": r.product_id,
            "rating": r.rating,
            "review_text": r.review_text,
            "created_at": r.created_at.isoformat() if r.created_at else None
        }
        for r in reviews
    ]), 200

@customer_bp.post("/reviews")
@role_required("CUSTOMER")
def create_review():
    data = request.get_json() or {}

    rating = data.get("rating")
    review_text = data.get("review_text")
    product_id = data.get("product_id")

    if rating is None or not review_text:
        return jsonify({
            "error": "rating and review_text are required"
        }), 400

    try:
        rating = int(rating)
    except (TypeError, ValueError):
        return jsonify({
            "error": "rating must be a number"
        }), 400

    if rating < 1 or rating > 5:
        return jsonify({
            "error": "rating must be between 1 and 5"
        }), 400

    if product_id:
        product = Product.query.get(product_id)

        if not product:
            return jsonify({
                "error": "Product not found"
            }), 404

        entrepreneur_id = product.entrepreneur_id
    else:
        entrepreneur_id = data.get("entrepreneur_id")

        if not entrepreneur_id:
            return jsonify({
                "error": "entrepreneur_id is required when product_id is not provided"
            }), 400

    review = Review(
        customer_id=current_user.id,
        entrepreneur_id=entrepreneur_id,
        product_id=product_id,
        rating=rating,
        review_text=review_text
    )

    try:
        db.session.add(review)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({
            "error": "Unable to create review"
        }), 500

    return jsonify({
        "message": "Review submitted successfully",
        "review_id": review.id
    }), 201
