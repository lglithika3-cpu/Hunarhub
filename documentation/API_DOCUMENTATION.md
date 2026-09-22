# HunarHub - API Documentation
## 1. Project Information
**Project Name:** HunarHub - Digital Marketplace for Local Micro-Entrepreneurs
**Backend Technology:** Python Flask
**Database:** MySQL
**Authentication:** Flask-Login Session Authentication
**Password Security:** Argon2id Password Hashing
**API Format:** REST-style JSON API
---
## 2. Base URL
For local development:
```text
http://127.0.0.1:5000
```
Frontend:
```text
http://127.0.0.1:5500
```
All API requests should use the backend base URL.
---
## 3. Authentication
HunarHub uses session-based authentication with Flask-Login.
After successful login, the authenticated session is maintained by the browser.
The frontend sends credentials with API requests.
Example:
```javascript
fetch("http://127.0.0.1:5000/me", {
&#x20;   credentials: "include"
});
```
---
# 4. Authentication APIs
## 4.1 Register User
**Endpoint:**
```text
POST /register
```
**Purpose:**
Creates a new HunarHub user account.
**Request Body:**
```json
{
&#x20;   "name": "New User",
&#x20;   "email": "user@example.com",
&#x20;   "phone": "9876543210",
&#x20;   "password": "StrongPassword@123",
&#x20;   "role": "CUSTOMER"
}
```
**Successful Response:**
```json
{
&#x20;   "message": "Registration successful"
}
```
**Possible Status Codes:**
* `201` - User registered successfully
* `400` - Invalid or missing information
* `409` - Email or phone already exists
---
## 4.2 Login User
**Endpoint:**
```text
POST /login
```
**Purpose:**
Authenticates a registered user.
**Request Body:**
```json
{
&#x20;   "email": "user@example.com",
&#x20;   "password": "StrongPassword@123"
}
```
**Successful Response:**
```json
{
&#x20;   "message": "Login successful",
&#x20;   "user": {
&#x20;       "id": 1,
&#x20;       "name": "New User",
&#x20;       "email": "user@example.com",
&#x20;       "role": "CUSTOMER"
&#x20;   }
}
```
**Possible Status Codes:**
* `200` - Login successful
* `400` - Invalid request
* `401` - Invalid email or password
---
## 4.3 Logout User
**Endpoint:**
```text
POST /logout
```
**Purpose:**
Logs out the currently authenticated user and clears the session.
**Successful Response:**
```json
{
&#x20;   "message": "Logout successful"
}
```
**Possible Status Codes:**
* `200` - Logout successful
* `401` - User is not authenticated
---
## 4.4 Get Current User
**Endpoint:**
```text
GET /me
```
**Purpose:**
Returns information about the currently logged-in user.
**Successful Response:**
```json
{
&#x20;   "id": 1,
&#x20;   "name": "New User",
&#x20;   "email": "user@example.com",
&#x20;   "role": "CUSTOMER"
}
```
**Possible Status Codes:**
* `200` - User information returned
* `401` - User is not authenticated
---
# 5. Customer APIs
Customer APIs are available to users with the `CUSTOMER` role.
## 5.1 Customer Dashboard
**Endpoint:**
```text
GET /customer/dashboard
```
**Purpose:**
Returns customer dashboard information.
---
## 5.2 Browse Products
**Endpoint:**
```text
GET /customer/products
```
**Purpose:**
Retrieves products available to customers.
**Example Response:**
```json
{
&#x20;   "products": \[
&#x20;       {
&#x20;           "id": 1,
&#x20;           "name": "Custom Shirt Stitching",
&#x20;           "price": 500,
&#x20;           "stock": 9,
&#x20;           "status": "ACTIVE"
&#x20;       }
&#x20;   ]
}
```
---
## 5.3 View Entrepreneur
**Endpoint:**
```text
GET /customer/entrepreneur/<entrepreneur\_id>
```
**Purpose:**
Displays the profile and business information of an entrepreneur.
**Example:**
```text
GET /customer/entrepreneur/2
```
---
## 5.4 View Product Details
**Endpoint:**
```text
GET /customer/products/<product\_id>
```
**Purpose:**
Returns detailed information about a particular product.
**Example:**
```text
GET /customer/products/1
```
---
## 5.5 Place Order
**Endpoint:**
```text
POST /customer/orders
```
**Purpose:**
Allows a customer to place an order for a product.
**Example Request:**
```json
{
&#x20;   "product\_id": 1,
&#x20;   "quantity": 1
}
```
**Example Response:**
```json
{
&#x20;   "message": "Order placed successfully"
}
```
---
## 5.6 View Customer Orders
**Endpoint:**
```text
GET /customer/orders
```
**Purpose:**
Returns orders belonging to the logged-in customer.
---
## 5.7 Create Service Request
**Endpoint:**
```text
POST /customer/service-requests
```
**Purpose:**
Allows customers to request a service from an entrepreneur.
**Example Request:**
```json
{
&#x20;   "service\_id": 1,
&#x20;   "request\_description": "I need a custom dress stitched.",
&#x20;   "preferred\_date": "2026-09-25"
}
```
---
## 5.8 View Service Requests
**Endpoint:**
```text
GET /customer/service-requests
```
**Purpose:**
Returns service requests created by the logged-in customer.
---
## 5.9 Submit Review
**Endpoint:**
```text
POST /customer/reviews
```
**Purpose:**
Allows customers to submit ratings and reviews.
**Example Request:**
```json
{
&#x20;   "entrepreneur\_id": 2,
&#x20;   "product\_id": 1,
&#x20;   "rating": 5,
&#x20;   "review\_text": "Good quality work."
}
```
---
## 5.10 View Customer Profile
**Endpoint:**
```text
GET /customer/profile
```
**Purpose:**
Returns the profile information of the logged-in customer.
---
## 5.11 Update Customer Profile
**Endpoint:**
```text
PUT /customer/profile
```
**Purpose:**
Updates customer profile information.
**Example Request:**
```json
{
&#x20;   "name": "Updated User",
&#x20;   "phone": "9876543210",
&#x20;   "language": "English"
}
```
---
# 6. Entrepreneur APIs
Entrepreneur APIs are available to users with the `ENTREPRENEUR` role.
## 6.1 Entrepreneur Dashboard
**Endpoint:**
```text
GET /entrepreneur/dashboard
```
**Purpose:**
Returns entrepreneur dashboard information.
---
## 6.2 View Entrepreneur Profile
**Endpoint:**
```text
GET /entrepreneur/profile
```
**Purpose:**
Returns the profile and business information of the logged-in entrepreneur.
---
## 6.3 Update Entrepreneur Profile
**Endpoint:**
```text
PUT /entrepreneur/profile
```
**Purpose:**
Updates entrepreneur business information.
**Example Request:**
```json
{
&#x20;   "business\_name": "Test Tailoring",
&#x20;   "bio": "Local tailoring service",
&#x20;   "skill\_description": "Tailoring and clothing alterations",
&#x20;   "experience": "2 years",
&#x20;   "address\_area": "Local Area",
&#x20;   "location\_visibility": "AREA\_ONLY",
&#x20;   "availability\_status": true
}
```
---
## 6.4 View Products
**Endpoint:**
```text
GET /entrepreneur/products
```
**Purpose:**
Returns products belonging to the logged-in entrepreneur.
---
## 6.5 Add Product
**Endpoint:**
```text
POST /entrepreneur/products
```
**Purpose:**
Creates a new product.
**Example Request:**
```json
{
&#x20;   "category\_id": 1,
&#x20;   "name": "Custom Shirt Stitching",
&#x20;   "description": "Custom shirt stitching service",
&#x20;   "price": 500,
&#x20;   "stock": 10,
&#x20;   "image\_url": "/images/custom-shirt.jpg"
}
```
---
## 6.6 Update Product
**Endpoint:**
```text
PUT /entrepreneur/products/<product\_id>
```
**Purpose:**
Updates an entrepreneur's own product.
**Example:**
```text
PUT /entrepreneur/products/1
```
---
## 6.7 Delete Product
**Endpoint:**
```text
DELETE /entrepreneur/products/<product\_id>
```
**Purpose:**
Deletes an entrepreneur's own product.
---
## 6.8 View Services
**Endpoint:**
```text
GET /entrepreneur/services
```
**Purpose:**
Returns services offered by the entrepreneur.
---
## 6.9 Add Service
**Endpoint:**
```text
POST /entrepreneur/services
```
**Purpose:**
Creates a new service.
**Example Request:**
```json
{
&#x20;   "category\_id": 1,
&#x20;   "name": "Custom Dress Stitching",
&#x20;   "description": "Custom dress stitching service",
&#x20;   "price": 800,
&#x20;   "estimated\_time": "3 Days",
&#x20;   "availability": true
}
```
---
## 6.10 Update Service
**Endpoint:**
```text
PUT /entrepreneur/services/<service\_id>
```
**Purpose:**
Updates an entrepreneur's own service.
---
## 6.11 Delete Service
**Endpoint:**
```text
DELETE /entrepreneur/services/<service\_id>
```
**Purpose:**
Deletes an entrepreneur's own service.
---
## 6.12 View Orders
**Endpoint:**
```text
GET /entrepreneur/orders
```
**Purpose:**
Returns orders associated with the entrepreneur.
---
## 6.13 Update Order
**Endpoint:**
```text
PUT /entrepreneur/orders/<order\_id>
```
**Purpose:**
Allows an entrepreneur to update the status of an order.
**Example Request:**
```json
{
&#x20;   "status": "CONFIRMED"
}
```
---
## 6.14 View Service Requests
**Endpoint:**
```text
GET /entrepreneur/service-requests
```
**Purpose:**
Returns service requests received by the entrepreneur.
---
## 6.15 Update Service Request
**Endpoint:**
```text
PUT /entrepreneur/service-requests/<request\_id>
```
**Purpose:**
Updates the status of a service request.
**Example Request:**
```json
{
&#x20;   "status": "ACCEPTED"
}
```
---
## 6.16 View Earnings
**Endpoint:**
```text
GET /entrepreneur/earnings
```
**Purpose:**
Returns earnings information for the entrepreneur.
---
# 7. Admin APIs
Admin APIs are available only to users with the `ADMIN` role.
## 7.1 Admin Dashboard
**Endpoint:**
```text
GET /admin/dashboard
```
**Purpose:**
Returns administrative dashboard information and statistics.
---
## 7.2 View Users
**Endpoint:**
```text
GET /admin/users
```
**Purpose:**
Returns registered users for administrative management.
---
## 7.3 Change User Role
**Endpoint:**
```text
PUT /admin/users/<user\_id>/role
```
**Purpose:**
Allows an administrator to change a user's role.
**Example Request:**
```json
{
&#x20;   "role": "ENTREPRENEUR"
}
```
---
## 7.4 View Entrepreneurs
**Endpoint:**
```text
GET /admin/entrepreneurs
```
**Purpose:**
Returns entrepreneurs for verification and management.
---
## 7.5 Update Entrepreneur Verification
**Endpoint:**
```text
PUT /admin/entrepreneurs/<entrepreneur\_id>/verification
```
**Purpose:**
Allows an administrator to verify or reject an entrepreneur.
**Example Request:**
```json
{
&#x20;   "verification\_status": "VERIFIED"
}
```
---
## 7.6 View Categories
**Endpoint:**
```text
GET /admin/categories
```
**Purpose:**
Returns all entrepreneur and product categories.
---
## 7.7 Add Category
**Endpoint:**
```text
POST /admin/categories
```
**Purpose:**
Creates a new marketplace category.
**Example Request:**
```json
{
&#x20;   "name": "Local Crafts",
&#x20;   "description": "Handcrafted products made by local artisans",
&#x20;   "status": "ACTIVE"
}
```
---
## 7.8 Update Category
**Endpoint:**
```text
PUT /admin/categories/<category\_id>
```
**Purpose:**
Updates an existing category.
---
## 7.9 View All Products
**Endpoint:**
```text
GET /admin/products
```
**Purpose:**
Returns all products for administrative monitoring.
---
## 7.10 Update Product Status
**Endpoint:**
```text
PUT /admin/products/<product\_id>/status
```
**Purpose:**
Allows an administrator to change product status.
**Example Request:**
```json
{
&#x20;   "status": "INACTIVE"
}
```
---
## 7.11 View All Services
**Endpoint:**
```text
GET /admin/services
```
**Purpose:**
Returns all services available in the system.
---
## 7.12 Update Service Status
**Endpoint:**
```text
PUT /admin/services/<service\_id>/status
```
**Purpose:**
Allows an administrator to change service status.
---
## 7.13 View All Orders
**Endpoint:**
```text
GET /admin/orders
```
**Purpose:**
Returns all orders for administrative monitoring.
---
## 7.14 Update Order Status
**Endpoint:**
```text
PUT /admin/orders/<order\_id>/status
```
**Purpose:**
Allows an administrator to update order status.
**Example Request:**
```json
{
&#x20;   "status": "COMPLETED"
}
```
---
## 7.15 View Service Requests
**Endpoint:**
```text
GET /admin/service-requests
```
**Purpose:**
Returns all service requests for administrative monitoring.
---
## 7.16 Update Service Request Status
**Endpoint:**
```text
PUT /admin/service-requests/<request\_id>/status
```
**Purpose:**
Allows an administrator to update service request status.
---
## 7.17 View Reviews
**Endpoint:**
```text
GET /admin/reviews
```
**Purpose:**
Returns customer reviews for administrative monitoring.
---
## 7.18 View Reports
**Endpoint:**
```text
GET /admin/reports
```
**Purpose:**
Returns marketplace statistics and reports.
---
# 8. Role-Based Access Control
HunarHub uses three main roles:
| Role         | Access                                                                                   |
| ------------ | ---------------------------------------------------------------------------------------- |
| CUSTOMER     | Marketplace, products, orders, service requests, reviews, profile                        |
| ENTREPRENEUR | Products, services, orders, service requests, earnings, business profile                 |
| ADMIN        | Users, entrepreneurs, categories, products, services, orders, requests, reviews, reports |
Unauthorized users cannot access protected role-specific APIs.
For example, a customer cannot access:
```text
GET /admin/users
```
A user without the required role receives an authorization error.
---
# 9. Ownership Protection
HunarHub also checks resource ownership.
For example:
* An entrepreneur can update their own products.
* An entrepreneur cannot update another entrepreneur's products.
* A customer can view their own orders.
* A customer cannot modify another customer's orders.
* Entrepreneurs can manage their own services and service requests.
This prevents users from accessing resources belonging to other users.
---
# 10. Password Security
Passwords are never stored as plain text.
HunarHub uses **Argon2id password hashing**.
During registration:
```text
Plain Password
&#x20;      |
&#x20;      v
Argon2id Hashing
&#x20;      |
&#x20;      v
Password Hash Stored in MySQL
```
During login:
```text
Entered Password
&#x20;      |
&#x20;      v
Argon2id Verification
&#x20;      |
&#x20;      v
Valid / Invalid
```
Only the password hash is stored in the database.
---
# 11. Session Security
After successful login, Flask-Login maintains the authenticated user session.
Protected endpoints require an authenticated session.
The frontend includes:
```text
credentials: "include"
```
with API requests so that the session cookie can be sent to the backend.
---
# 12. JSON Format
Most API requests and responses use JSON.
Request header:
```text
Content-Type: application/json
```
Example:
```json
{
&#x20;   "name": "Example User",
&#x20;   "role": "CUSTOMER"
}
```
---
# 13. Common HTTP Status Codes
| Status Code | Meaning                                          |
| ----------- | ------------------------------------------------ |
| 200         | Request successful                               |
| 201         | Resource created successfully                    |
| 400         | Bad request or invalid data                      |
| 401         | Authentication required or authentication failed |
| 403         | Access denied                                    |
| 404         | Resource not found                               |
| 409         | Duplicate resource or conflicting data           |
| 500         | Internal server error                            |
---
# 14. API Testing with Postman
The APIs can be tested using Postman.
Recommended testing sequence:
### Step 1 - Register
```text
POST /register
```
### Step 2 - Login
```text
POST /login
```
### Step 3 - Check Session
```text
GET /me
```
### Step 4 - Test Role-Specific APIs
For a customer:
```text
GET /customer/dashboard
GET /customer/products
GET /customer/orders
GET /customer/service-requests
```
For an entrepreneur:
```text
GET /entrepreneur/dashboard
GET /entrepreneur/products
GET /entrepreneur/services
GET /entrepreneur/orders
GET /entrepreneur/earnings
```
For an administrator:
```text
GET /admin/dashboard
GET /admin/users
GET /admin/categories
GET /admin/products
GET /admin/orders
GET /admin/reports
```
### Step 5 - Test Authorization
Try accessing another role's endpoint.
The system should reject unauthorized access.
---
# 15. API Security Features
HunarHub API security includes:
* Argon2id password hashing
* Flask-Login session authentication
* Role-Based Access Control
* Login-required protected routes
* Role-specific route protection
* Ownership validation
* Admin-only management APIs
* Session-based authentication
* JSON request validation
* MySQL database access through Flask-SQLAlchemy
---
# 16. Complete API Endpoint Summary
## Authentication
```text
POST   /register
POST   /login
POST   /logout
GET    /me
```
## Customer
```text
GET    /customer/dashboard
GET    /customer/products
GET    /customer/entrepreneur/<entrepreneur\_id>
GET    /customer/products/<product\_id>
POST   /customer/orders
GET    /customer/orders
POST   /customer/service-requests
GET    /customer/service-requests
POST   /customer/reviews
GET    /customer/profile
PUT    /customer/profile
```
## Entrepreneur
```text
GET    /entrepreneur/dashboard
GET    /entrepreneur/profile
PUT    /entrepreneur/profile
GET    /entrepreneur/products
POST   /entrepreneur/products
PUT    /entrepreneur/products/<product\_id>
DELETE /entrepreneur/products/<product\_id>
GET    /entrepreneur/services
POST   /entrepreneur/services
PUT    /entrepreneur/services/<service\_id>
DELETE /entrepreneur/services/<service\_id>
GET    /entrepreneur/orders
PUT    /entrepreneur/orders/<order\_id>
GET    /entrepreneur/service-requests
PUT    /entrepreneur/service-requests/<request\_id>
GET    /entrepreneur/earnings
```
## Admin
```text
GET    /admin/dashboard
GET    /admin/users
PUT    /admin/users/<user\_id>/role
GET    /admin/entrepreneurs
PUT    /admin/entrepreneurs/<entrepreneur\_id>/verification
GET    /admin/categories
POST   /admin/categories
PUT    /admin/categories/<category\_id>
GET    /admin/products
PUT    /admin/products/<product\_id>/status
GET    /admin/services
PUT    /admin/services/<service\_id>/status
GET    /admin/orders
PUT    /admin/orders/<order\_id>/status
GET    /admin/service-requests
PUT    /admin/service-requests/<request\_id>/status
GET    /admin/reviews
GET    /admin/reports
```
---
# 17. API Documentation Summary
The HunarHub API provides the backend interface for the complete digital marketplace.
The API supports:
* User registration and login
* Session authentication
* Customer marketplace operations
* Product browsing and ordering
* Service requests
* Reviews and ratings
* Entrepreneur product management
* Entrepreneur service management
* Order management
* Earnings information
* Administrator management
* Category management
* Entrepreneur verification
* Reports and statistics
* Role-Based Access Control
* Ownership protection
* Secure password storage
The API is designed to provide secure communication between the HunarHub frontend, backend, and MySQL database.
