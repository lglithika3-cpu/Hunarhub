from backend.app import app

app.config["TESTING"] = True

def check_login(client, email):
    response = client.post("/login", json={
        "email": email,
        "password": "Test@12345"
    })
    print("LOGIN", email, "=>", response.status_code)
    return response.status_code == 200

customer = app.test_client()
entrepreneur = app.test_client()
admin = app.test_client()

customer_ok = check_login(customer, "test_hh_2026_customer@test.com")
entrepreneur_ok = check_login(entrepreneur, "test_hh_2026_entrepreneur@test.com")
admin_ok = check_login(admin, "test_hh_2026_admin@test.com")

print("\nLOGIN STATUS")
print("Customer:", customer_ok)
print("Entrepreneur:", entrepreneur_ok)
print("Admin:", admin_ok)

print("\nROLE ACCESS TEST")

tests = [
    (customer, "/customer/dashboard", "CUSTOMER -> CUSTOMER"),
    (customer, "/entrepreneur/dashboard", "CUSTOMER -> ENTREPRENEUR"),
    (customer, "/admin/dashboard", "CUSTOMER -> ADMIN"),
    (entrepreneur, "/entrepreneur/dashboard", "ENTREPRENEUR -> ENTREPRENEUR"),
    (entrepreneur, "/customer/dashboard", "ENTREPRENEUR -> CUSTOMER"),
    (entrepreneur, "/admin/dashboard", "ENTREPRENEUR -> ADMIN"),
    (admin, "/admin/dashboard", "ADMIN -> ADMIN"),
    (admin, "/customer/dashboard", "ADMIN -> CUSTOMER"),
]

for client, route, description in tests:
    response = client.get(route)
    print(response.status_code, description)

print("\nUNAUTHENTICATED TEST")

guest = app.test_client()

for route in [
    "/customer/dashboard",
    "/entrepreneur/dashboard",
    "/admin/dashboard"
]:
    response = guest.get(route)
    print(response.status_code, route)

print("\n========== RBAC TEST COMPLETE ==========")
