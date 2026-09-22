from backend.app import app

app.testing = True

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

print("\n========== STEP 10: UNAUTHENTICATED PROTECTION ==========")

step10 = True

with app.test_client() as client:
    with client.session_transaction() as sess:
        sess.clear()

    with client.session_transaction() as sess:
        print("TEST SESSION:", dict(sess))

    for route in customer_routes + entrepreneur_routes + admin_routes:
        with client.session_transaction() as sess:
            sess.clear()

        response = client.get(
            route,
            follow_redirects=False
        )

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

if step10:
    print("\n========== STEP 10 FINISHED ==========")
else:
    print("\n========== STEP 10 STILL HAS FAILURES ==========")
