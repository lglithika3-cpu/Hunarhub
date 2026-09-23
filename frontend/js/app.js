const API_BASE_URL = "http://127.0.0.1:5000";

async function apiRequest(endpoint, options = {}) {
    const response = await fetch(API_BASE_URL + endpoint, {
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            ...(options.headers || {})
        },
        ...options
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok) {
        throw new Error(data.error || data.message || "Request failed");
    }

    return data;
}

async function getCurrentUser() {
    try {
        return await apiRequest("/me");
    } catch {
        return null;
    }
}

function redirectByRole(user) {
    if (!user) {
        window.location.href = "/login.html";
        return;
    }

    const role = String(user.role).toUpperCase();

    if (role === "CUSTOMER") {
        window.location.href = "customer/dashboard.html";
    } else if (role === "ENTREPRENEUR") {
        window.location.href = "entrepreneur/dashboard.html";
    } else if (role === "ADMIN") {
        window.location.href = "admin/dashboard.html";
    }
}

async function logout() {
    try {
        await apiRequest("/logout", {
            method: "POST"
        });
    } finally {
        window.location.href = "/login.html";
    }
}
