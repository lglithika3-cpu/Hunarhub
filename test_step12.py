from pathlib import Path

print("\n========================================")
print("STEP 12: FRONTEND TESTING")
print("========================================")

step12 = True

frontend = Path("frontend")

if not frontend.exists():
    print("frontend folder -> MISSING [FAIL]")
    step12 = False
else:
    print("frontend folder -> EXISTS [PASS]")

expected_files = [
    "index.html",
    "login.html",
    "register.html",
    "marketplace.html",
    "entrepreneur.html",
    "products.html",
    "requests.html",
    "profile.html"
]

print("\n========== REQUIRED FRONTEND PAGES ==========")

for filename in expected_files:
    path = frontend / filename

    if path.exists():
        print(f"{filename} -> EXISTS [PASS]")
    else:
        print(f"{filename} -> MISSING [FAIL]")
        step12 = False

html_files = list(frontend.rglob("*.html"))
css_files = list(frontend.rglob("*.css"))
js_files = list(frontend.rglob("*.js"))

print("\n========== FRONTEND FILE COUNTS ==========")
print(f"HTML files -> {len(html_files)}")
print(f"CSS files -> {len(css_files)}")
print(f"JavaScript files -> {len(js_files)}")

if len(html_files) > 0:
    print("HTML files -> PASS")
else:
    print("HTML files -> FAIL")
    step12 = False

if len(css_files) > 0:
    print("CSS files -> PASS")
else:
    print("CSS files -> WARNING")

if len(js_files) > 0:
    print("JavaScript files -> PASS")
else:
    print("JavaScript files -> WARNING")

print("\n========== HTML CONTENT CHECK ==========")

empty_files = []

for html_file in html_files:
    try:
        content = html_file.read_text(
            encoding="utf-8",
            errors="ignore"
        ).strip()

        if len(content) == 0:
            empty_files.append(str(html_file))
            print(f"{html_file} -> EMPTY [FAIL]")
        else:
            print(f"{html_file} -> CONTENT FOUND [PASS]")

    except Exception as e:
        empty_files.append(str(html_file))
        print(f"{html_file} -> READ ERROR [FAIL]")
        print(str(e))

if empty_files:
    step12 = False

print("\n========== IMPORTANT FRONTEND PAGES ==========")

important_pages = [
    "index.html",
    "login.html",
    "register.html",
    "marketplace.html",
    "entrepreneur.html",
    "products.html",
    "requests.html",
    "profile.html"
]

for filename in important_pages:
    path = frontend / filename

    if not path.exists():
        continue

    content = path.read_text(
        encoding="utf-8",
        errors="ignore"
    ).lower()

    if len(content.strip()) > 0:
        print(f"{filename} -> PAGE CONTENT PASS")
    else:
        print(f"{filename} -> PAGE CONTENT FAIL")
        step12 = False

print("\n========== CSS / JS REFERENCES ==========")

all_html_content = ""

for html_file in html_files:
    try:
        all_html_content += "\n" + html_file.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()
    except Exception:
        pass

if css_files:
    print("CSS resource exists -> PASS")
else:
    print("CSS resource -> WARNING")

if js_files:
    print("JavaScript resource exists -> PASS")
else:
    print("JavaScript resource -> WARNING")

print("\n========== BACKEND REFERENCES ==========")

backend_reference_checks = [
    ("/login", "Login"),
    ("/register", "Register"),
    ("/entrepreneur", "Entrepreneur"),
    ("/admin", "Admin")
]

for keyword, name in backend_reference_checks:
    if keyword in all_html_content:
        print(f"{name} reference -> FOUND [PASS]")
    else:
        print(f"{name} reference -> NOT FOUND [WARNING]")

print("\n========== SERVICE REQUEST PAGE CHECK ==========")

service_request_files = [
    frontend / "requests.html",
    frontend / "customer" / "service-requests.html",
    frontend / "pages" / "service-requests.html"
]

service_request_found = False

for path in service_request_files:
    if path.exists():
        content = path.read_text(
            encoding="utf-8",
            errors="ignore"
        ).lower()

        if "service" in content or "request" in content:
            print(f"{path} -> SERVICE REQUEST CONTENT FOUND [PASS]")
            service_request_found = True

if not service_request_found:
    for html_file in html_files:
        try:
            content = html_file.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "service request" in content or "service-requests" in content:
                print(f"{html_file} -> SERVICE REQUEST CONTENT FOUND [PASS]")
                service_request_found = True
                break
        except Exception:
            pass

if not service_request_found:
    print("Service request page -> NOT FOUND [WARNING]")

print("\n========== FINAL STEP 12 RESULT ==========")

print("STEP 12:", "PASS" if step12 else "FAIL")

if step12:
    print("\n========== STEP 12 COMPLETED ==========")
else:
    print("\n========== STEP 12 STILL HAS FAILURES ==========")
