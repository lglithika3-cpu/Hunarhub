from backend.app import app
from backend.database import db
from backend.models.user import User
from sqlalchemy import text

app.testing = True

PASSWORD = "Test@12345"

def check(label, response, expected):
    status = response.status_code
    result = "PASS" if status == expected else "FAIL"
    print(f"{label} -> {status} [{result}]")
    return status == expected

def login(client, email):
    response = client.post(
        "/login",
        json={
            "email": email,
            "password": PASSWORD
        }
    )
    print(f"LOGIN {email} -> {response.status_code}")
    return response.status_code == 200

with app.app_context():
    db.session.rollback()

    customer = User.query.filter_by(
        email="test_hh_2026_customer@test.com"
    ).first()

    entrepreneur = User.query.filter_by(
        email="test_hh_2026_entrepreneur@test.com"
    ).first()

    admin = User.query.filter_by(
        email="test_hh_2026_admin@test.com"
    ).first()

    print("\n========== STEPS 6-10 ==========")

    if not customer or not entrepreneur or not admin:
        print("ERROR: Required test users not found.")
        raise SystemExit(1)

    print("\nTEST USERS")
    print(f"CUSTOMER: {customer.email} -> {customer.role}")
    print(f"ENTREPRENEUR: {entrepreneur.email} -> {entrepreneur.role}")
    print(f"ADMIN: {admin.email} -> {admin.role}")

    customer_routes = [
        "/api/customer/profile",
        "/api/customer/products",
        "/api/customer/services",
        "/api/customer/orders",
        "/api/customer/service-requests",
        "/api/customer/reviews"
    ]

    entrepreneur_routes = [
        "/entrepreneur/dashboard",
        "/entrepreneur/products",
        "/entrepreneur/services",
        "/entrepreneur/orders",
        "/entrepreneur/service-requests",
        "/entrepreneur/earnings",
        "/entrepreneur/profile"
    ]

    admin_routes = [
        "/admin/dashboard",
        "/admin/users",
        "/admin/products",
        "/admin/services",
        "/admin/orders",
        "/admin/service-requests",
        "/admin/reports",
        "/admin/categories",
        "/admin/reviews"
    ]

    print("\n========== STEP 6: AUTHENTICATED RBAC ==========")

    step6 = True

    customer_client = app.test_client()

    if not login(
        customer_client,
        "test_hh_2026_customer@test.com"
    ):
        print("CUSTOMER LOGIN FAILED")
        step6 = False
    else:
        print("\nCUSTOMER RBAC")

        for route in customer_routes:
            if not check(
                f"CUSTOMER -> {route}",
                customer_client.get(route),
                200
            ):
                step6 = False

        for route in entrepreneur_routes:
            if not check(
                f"CUSTOMER blocked -> {route}",
                customer_client.get(route),
                403
            ):
                step6 = False

        for route in admin_routes:
            if not check(
                f"CUSTOMER blocked -> {route}",
                customer_client.get(route),
                403
            ):
                step6 = False

    entrepreneur_client = app.test_client()

    if not login(
        entrepreneur_client,
        "test_hh_2026_entrepreneur@test.com"
    ):
        print("ENTREPRENEUR LOGIN FAILED")
        step6 = False
    else:
        print("\nENTREPRENEUR RBAC")

        for route in entrepreneur_routes:
            if not check(
                f"ENTREPRENEUR -> {route}",
                entrepreneur_client.get(route),
                200
            ):
                step6 = False

        for route in customer_routes:
            if not check(
                f"ENTREPRENEUR blocked -> {route}",
                entrepreneur_client.get(route),
                403
            ):
                step6 = False

        for route in admin_routes:
            if not check(
                f"ENTREPRENEUR blocked -> {route}",
                entrepreneur_client.get(route),
                403
            ):
                step6 = False

    admin_client = app.test_client()

    if not login(
        admin_client,
        "test_hh_2026_admin@test.com"
    ):
        print("ADMIN LOGIN FAILED")
        step6 = False
    else:
        print("\nADMIN RBAC")

        for route in admin_routes:
            if not check(
                f"ADMIN -> {route}",
                admin_client.get(route),
                200
            ):
                step6 = False

        for route in customer_routes:
            if not check(
                f"ADMIN blocked -> {route}",
                admin_client.get(route),
                403
            ):
                step6 = False

        for route in entrepreneur_routes:
            if not check(
                f"ADMIN blocked -> {route}",
                admin_client.get(route),
                403
            ):
                step6 = False

    print("\nSTEP 6 RESULT:", "PASS" if step6 else "FAIL")

    print("\n========== STEP 7: CRUD / VALIDATION ==========")

    step7 = True

    customer_client = app.test_client()

    if not login(
        customer_client,
        "test_hh_2026_customer@test.com"
    ):
        print("CUSTOMER LOGIN FAILED")
        step7 = False
    else:
        tests = [
            ("/api/customer/orders", {}, 400),
            ("/api/customer/service-requests", {}, 400),
            ("/api/customer/reviews", {}, 400)
        ]

        for route, body, expected in tests:
            if not check(
                f"Invalid POST {route}",
                customer_client.post(route, json=body),
                expected
            ):
                step7 = False

        response = customer_client.post(
            "/api/customer/orders",
            json={
                "items": [
                    {
                        "product_id": 999999,
                        "quantity": 1
                    }
                ]
            }
        )

        if not check(
            "Invalid product order",
            response,
            404
        ):
            step7 = False

        response = customer_client.post(
            "/api/customer/reviews",
            json={
                "entrepreneur_id": 999999,
                "rating": 6,
                "review_text": "Invalid review"
            }
        )

        if not check(
            "Invalid review rating",
            response,
            400
        ):
            step7 = False

    db.session.rollback()

    print("\nSTEP 7 RESULT:", "PASS" if step7 else "FAIL")

    print("\n========== STEP 8: ROUTE CHECK ==========")

    required_routes = [
        "/login",
        "/register",
        "/logout",
        "/me",
        "/api/customer/profile",
        "/api/customer/products",
        "/api/customer/services",
        "/api/customer/orders",
        "/api/customer/service-requests",
        "/api/customer/reviews",
        "/entrepreneur/dashboard",
        "/entrepreneur/products",
        "/entrepreneur/services",
        "/entrepreneur/orders",
        "/entrepreneur/service-requests",
        "/entrepreneur/earnings",
        "/admin/dashboard",
        "/admin/users",
        "/admin/products",
        "/admin/services",
        "/admin/orders",
        "/admin/service-requests",
        "/admin/reports",
        "/admin/categories",
        "/admin/reviews"
    ]

    existing_routes = {
        str(rule.rule)
        for rule in app.url_map.iter_rules()
    }

    step8 = True

    for route in required_routes:
        if route in existing_routes:
            print(f"{route} -> EXISTS [PASS]")
        else:
            print(f"{route} -> MISSING [FAIL]")
            step8 = False

    print("\nSTEP 8 RESULT:", "PASS" if step8 else "FAIL")

    print("\n========== STEP 9: PASSWORD SECURITY ==========")

    db.session.rollback()

    rows = db.session.execute(
        text("SELECT email, password_hash FROM users")
    ).fetchall()

    step9 = True

    for row in rows:
        password_hash = row.password_hash or ""

        if password_hash.startswith("$argon2") or password_hash.startswith("$2"):
            print(f"{row.email} -> HASHED [PASS]")
        else:
            print(f"{row.email} -> UNKNOWN HASH [FAIL]")
            step9 = False

    print("\nSTEP 9 RESULT:", "PASS" if step9 else "FAIL")

    print("\n========== STEP 10: UNAUTHENTICATED PROTECTION ==========")

    step10 = True

    unauthenticated_client = app.test_client()

    for route in customer_routes + entrepreneur_routes + admin_routes:
        response = unauthenticated_client.get(route)

        if response.status_code in [401, 302]:
            print(
                f"{route} -> {response.status_code} [PASS]"
            )
        else:
            print(
                f"{route} -> {response.status_code} [FAIL]"
            )
            step10 = False

    print("\nSTEP 10 RESULT:", "PASS" if step10 else "FAIL")

    print("\n========================================")
    print("FINAL STEPS 6-10 RESULTS")
    print("========================================")
    print("STEP 6:", "PASS" if step6 else "FAIL")
    print("STEP 7:", "PASS" if step7 else "FAIL")
    print("STEP 8:", "PASS" if step8 else "FAIL")
    print("STEP 9:", "PASS" if step9 else "FAIL")
    print("STEP 10:", "PASS" if step10 else "FAIL")

    if all([step6, step7, step8, step9, step10]):
        print("\n========== STEPS 6-10 FINISHED ==========")
    else:
        print("\n========== STEPS 6-10 HAVE FAILURES ==========")
