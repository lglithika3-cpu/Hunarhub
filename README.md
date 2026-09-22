\# HunarHub – Digital Marketplace for Local Micro-Entrepreneurs



\## Project Overview



HunarHub is a web-based digital marketplace designed to connect local micro-entrepreneurs with customers through a simple and secure online platform.



The platform helps local professionals such as tailors, potters, cobblers, artisans, handmade-product sellers, and local vendors showcase their products and services. Customers can discover entrepreneurs, browse products, place orders, request services, track their activities, and provide reviews.



HunarHub also provides separate interfaces for customers, entrepreneurs, and administrators with role-based access control.



\## Objectives



The main objectives of HunarHub are:



\* Connect local micro-entrepreneurs with customers through a digital marketplace.

\* Provide entrepreneurs with an online platform to manage products and services.

\* Allow customers to search and browse locally available products and services.

\* Support product ordering and service-request management.

\* Provide order and service-request tracking.

\* Enable customer reviews and ratings.

\* Protect user accounts using secure password hashing.

\* Implement role-based access control for different users.

\* Provide administrators with tools to manage users, entrepreneurs, products, services, orders, reviews, and reports.

\* Support privacy-aware location information for entrepreneurs.



\## User Roles



\### CUSTOMER



Customers can:



\* Register and log in.

\* Browse products.

\* Search and filter marketplace products.

\* View entrepreneur profiles.

\* View product details.

\* Place product orders.

\* Track orders.

\* Submit service requests.

\* Track service requests.

\* Submit reviews and ratings.

\* Manage their profile.



\### ENTREPRENEUR



Entrepreneurs can:



\* Manage their business profile.

\* Add business information.

\* Describe skills and experience.

\* Manage availability.

\* Add and manage products.

\* Add and manage services.

\* View and update customer orders.

\* Manage service requests.

\* View earnings.



\### ADMIN



Administrators can:



\* View the administration dashboard.

\* Manage users.

\* Change user roles.

\* Verify entrepreneurs.

\* Manage categories.

\* Manage products.

\* Manage services.

\* Manage orders.

\* Manage service requests.

\* Manage reviews.

\* View reports and statistics.



\## Entrepreneur Categories



HunarHub supports local micro-entrepreneurs from different categories:



1\. Tailor

2\. Potter

3\. Cobbler

4\. Artisan

5\. Handmade Products

6\. Local Vendor



\## Main Features



\### Authentication



The system provides:



\* User registration.

\* User login.

\* User logout.

\* Session-based authentication.

\* Current-user verification.



\### Password Security



User passwords are not stored as plain text.



HunarHub uses Argon2 password hashing to securely store passwords and verify login credentials.



\### Role-Based Access Control



Different users receive access according to their roles:



```text

CUSTOMER

&#x20;   ↓

Customer Features



ENTREPRENEUR

&#x20;   ↓

Entrepreneur Features



ADMIN

&#x20;   ↓

Administrative Features

```



Protected backend routes ensure that users cannot access functions belonging to unauthorized roles.



\### Marketplace



Customers can browse products offered by local entrepreneurs.



Product information includes:



\* Product name.

\* Description.

\* Price.

\* Stock availability.

\* Category.

\* Product image.

\* Product status.



\### Orders



Customers can place product orders and view their order history.



Entrepreneurs can view customer orders and update order status.



Supported order statuses include:



```text

PENDING

CONFIRMED

COMPLETED

CANCELLED

```



\### Service Requests



Customers can request services from entrepreneurs.



Service requests support:



```text

PENDING

ACCEPTED

REJECTED

COMPLETED

CANCELLED

```



\### Reviews and Ratings



Customers can provide ratings and reviews for products and entrepreneurs after receiving services or products.



\### Privacy-Aware Location



Entrepreneur location information can be controlled through visibility settings:



```text

EXACT

AREA\_ONLY

HIDDEN

```



This allows the system to avoid unnecessarily exposing exact location information.



\## Technology Stack



\### Frontend



\* HTML5

\* CSS3

\* JavaScript



\### Backend



\* Python

\* Flask

\* Flask-Login

\* Flask-SQLAlchemy

\* Flask-CORS



\### Database



\* MySQL

\* SQLAlchemy

\* PyMySQL



\### Security



\* Argon2 password hashing

\* Flask-Login authentication

\* Role-Based Access Control

\* Session-based authentication

\* Ownership checks

\* Protected role-specific routes



\### Development Tools



\* PyCharm

\* Visual Studio Code

\* MySQL Workbench

\* Git/GitHub

\* Postman



\## Project Structure



```text

HunarHub/

│

├── backend/

│   ├── app.py

│   ├── config.py

│   ├── database.py

│   │

│   ├── models/

│   │   ├── user.py

│   │   ├── product.py

│   │   ├── ...

│   │

│   ├── routes/

│   │   ├── auth.py

│   │   ├── customer.py

│   │   ├── entrepreneur.py

│   │   ├── admin.py

│   │   └── ...

│   │

│   ├── security/

│   │   ├── password.py

│   │   └── roles.py

│   │

│   └── services/

│

├── frontend/

│   ├── index.html

│   ├── login.html

│   ├── register.html

│   │

│   ├── customer/

│   │   ├── dashboard.html

│   │   ├── entrepreneur.html

│   │   ├── marketplace.html

│   │   ├── orders.html

│   │   ├── product.html

│   │   ├── profile.html

│   │   ├── review.html

│   │   └── service-requests.html

│   │

│   ├── entrepreneur/

│   │   ├── dashboard.html

│   │   ├── earnings.html

│   │   ├── orders.html

│   │   ├── products.html

│   │   ├── profile.html

│   │   ├── service-requests.html

│   │   └── services.html

│   │

│   ├── admin/

│   │   ├── dashboard.html

│   │   ├── users.html

│   │   ├── entrepreneurs.html

│   │   ├── categories.html

│   │   ├── products.html

│   │   ├── services.html

│   │   ├── orders.html

│   │   ├── service-requests.html

│   │   ├── reviews.html

│   │   └── reports.html

│   │

│   ├── css/

│   │   └── style.css

│   │

│   ├── js/

│   │   └── app.js

│   │

│   └── images/

│

├── screenshots/

├── documentation/

├── README.md

├── .env

└── venv/

```



\## Database Design



The main database tables are:



```text

users

categories

entrepreneurs

products

services

orders

order\_items

service\_requests

reviews

```



\### Users



Stores customer, entrepreneur, and administrator account information.



\### Categories



Stores marketplace categories for local products and services.



\### Entrepreneurs



Stores entrepreneur business profiles, skills, experience, availability, and privacy-aware location information.



\### Products



Stores products created by entrepreneurs.



\### Services



Stores services offered by entrepreneurs.



\### Orders



Stores customer product orders and order status.



\### Order Items



Stores individual products included in an order.



\### Service Requests



Stores customer requests for entrepreneur services.



\### Reviews



Stores customer ratings and reviews.



\## Application Flow



```text

User

&#x20;│

&#x20;├── Register

&#x20;│

&#x20;└── Login

&#x20;      │

&#x20;      ▼

&#x20;  Authentication

&#x20;      │

&#x20;      ▼

&#x20;  Role Detection

&#x20;      │

&#x20;┌─────┼─────────────┐

&#x20;▼     ▼             ▼

CUSTOMER ENTREPRENEUR ADMIN

&#x20;│       │             │

&#x20;▼       ▼             ▼

Browse   Manage       Manage

Products Products     Users

Orders   Services     Categories

Services Orders       Products

Reviews  Requests     Services

Profile  Earnings     Orders

&#x20;                    Reports

```



\## API Modules



\### Authentication



```text

POST /register

POST /login

POST /logout

GET  /me

```



\### Customer



```text

GET  /customer/dashboard

GET  /customer/products

GET  /customer/entrepreneur/<entrepreneur\_id>

GET  /customer/products/<product\_id>

POST /customer/orders

GET  /customer/orders

POST /customer/service-requests

GET  /customer/service-requests

POST /customer/reviews

GET  /customer/profile

PUT  /customer/profile

```



\### Entrepreneur



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



\### Admin



```text

GET  /admin/dashboard

GET  /admin/users

PUT  /admin/users/<user\_id>/role

GET  /admin/entrepreneurs

PUT  /admin/entrepreneurs/<entrepreneur\_id>/verification

GET  /admin/categories

POST /admin/categories

PUT  /admin/categories/<category\_id>

GET  /admin/products

PUT  /admin/products/<product\_id>/status

GET  /admin/services

PUT  /admin/services/<service\_id>/status

GET  /admin/orders

PUT  /admin/orders/<order\_id>/status

GET  /admin/service-requests

PUT  /admin/service-requests/<request\_id>/status

GET  /admin/reviews

GET  /admin/reports

```



\## Running the Project



\### 1. Activate the Virtual Environment



Open PowerShell and run:



```powershell

cd C:\\Users\\HP\\Desktop\\HunarHub

\& ".\\venv\\Scripts\\Activate.ps1"

```



\### 2. Start the Flask Backend



Open a PowerShell terminal:



```powershell

cd C:\\Users\\HP\\Desktop\\HunarHub

\& ".\\venv\\Scripts\\Activate.ps1"

cd backend

python -m flask --app app run

```



The backend runs at:



```text

http://127.0.0.1:5000

```



\### 3. Start the Frontend



Open another PowerShell terminal:



```powershell

cd C:\\Users\\HP\\Desktop\\HunarHub

py -m http.server 5500 --directory frontend

```



The frontend runs at:



```text

http://127.0.0.1:5500

```



\### 4. Open HunarHub



Open the following address in a browser:



```text

http://127.0.0.1:5500

```



\## Testing



The project was tested at multiple levels:



\* Backend route verification.

\* Database connectivity verification.

\* Authentication testing.

\* Password hashing verification.

\* Role-based access control testing.

\* Customer functionality testing.

\* Entrepreneur functionality testing.

\* Admin functionality testing.

\* Frontend API integration testing.

\* Product image loading verification.

\* Full-system integration testing.



\## Current Frontend Page Count



```text

Customer Pages      : 8

Entrepreneur Pages  : 7

Admin Pages         : 10

```



Total role-specific pages:



```text

25

```



\## Product Images



The marketplace supports product images for products such as:



\* Custom Shirt Stitching

\* Custom Kurta Stitching

\* Pottery

\* Leather Shoes

\* Handmade Products

\* Artisan Products



Images are stored in:



```text

frontend/images/

```



\## Security Considerations



HunarHub includes several security mechanisms:



\* Passwords are stored using Argon2 hashing.

\* Authentication is handled using Flask-Login.

\* Role-based authorization protects restricted routes.

\* Ownership checks help prevent users from modifying resources belonging to other users.

\* Administrative functionality is restricted to administrators.

\* Session credentials are handled through authenticated requests.

\* Location visibility provides privacy-aware location control.



\## Limitations



The current version is a prototype-level web application.



Potential future improvements include:



\* Online payment integration.

\* Email and SMS notifications.

\* Advanced search.

\* More detailed analytics.

\* Improved mobile responsiveness.

\* Image upload management.

\* Real-time order notifications.

\* Deployment to a production server.

\* Stronger production-level security configuration.

\* Backup and recovery mechanisms.



\## Future Enhancements



Future versions of HunarHub can include:



\* Mobile application support.

\* Multilingual interface.

\* Improved entrepreneur discovery.

\* Advanced marketplace filters.

\* Digital payment integration.

\* Notification systems.

\* Delivery tracking.

\* Enhanced analytics dashboards.

\* Customer support functionality.

\* Improved accessibility.



\## Project Status



```text

Project Setup              ✓ Completed

Database                   ✓ Completed

Backend                    ✓ Completed

Authentication             ✓ Completed

Password Security          ✓ Completed

RBAC                       ✓ Completed

Customer Module            ✓ Completed

Entrepreneur Module        ✓ Completed

Admin Module               ✓ Completed

Frontend                   ✓ Completed

API Integration             ✓ Completed

Full-System Testing        ✓ Completed

Image Integration          ✓ Completed

Documentation Structure    ✓ Completed

```



\## Conclusion



HunarHub provides a digital platform for connecting customers with local micro-entrepreneurs. The system combines marketplace functionality, product and service management, order processing, service requests, reviews, authentication, role-based access control, and privacy-aware location handling in a single web application.



The project demonstrates how a full-stack web application can be developed to support local businesses while maintaining structured access control and basic security practices.



\## Project Information



\*\*Project Name:\*\* HunarHub



\*\*Project Title:\*\* Digital Marketplace for Local Micro-Entrepreneurs



\*\*Application Type:\*\* Full-Stack Web Application



\*\*Frontend:\*\* HTML, CSS, JavaScript



\*\*Backend:\*\* Python Flask



\*\*Database:\*\* MySQL



\*\*Authentication:\*\* Flask-Login



\*\*Password Security:\*\* Argon2



\*\*Access Control:\*\* Role-Based Access Control



\*\*Primary Roles:\*\* Customer, Entrepreneur, Admin



