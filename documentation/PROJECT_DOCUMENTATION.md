\# HunarHub - Project Documentation



\## 1. Project Title



\*\*HunarHub - Digital Marketplace for Local Micro-Entrepreneurs\*\*



\## 2. Project Overview



HunarHub is a full-stack web application designed to provide a digital marketplace for local micro-entrepreneurs.



The platform connects customers with local entrepreneurs such as tailors, potters, cobblers, artisans, handmade-product sellers, and local vendors.



Customers can discover products and services, place orders, request services, track activities, and submit reviews. Entrepreneurs can manage their business profiles, products, services, orders, service requests, and earnings. Administrators can manage users, entrepreneurs, categories, products, services, orders, reviews, and reports.



The system uses authentication and role-based access control to provide different functionality according to the user's role.



\## 3. Problem Statement



Many local micro-entrepreneurs depend mainly on offline customers and traditional methods to promote and manage their businesses.



Customers may also find it difficult to discover local service providers and compare their available products or services.



HunarHub addresses this problem by providing a centralized digital platform where local entrepreneurs can present their products and services while customers can interact with them through an online marketplace.



\## 4. Objectives



The objectives of HunarHub are:



\* To create a digital marketplace for local micro-entrepreneurs.

\* To connect customers with local entrepreneurs.

\* To allow entrepreneurs to manage their products and services.

\* To provide customers with product browsing and ordering functionality.

\* To support service-request management.

\* To provide order and service-request tracking.

\* To support customer reviews and ratings.

\* To implement secure user authentication.

\* To protect passwords using Argon2 hashing.

\* To implement role-based access control.

\* To provide administrators with centralized management functionality.

\* To provide privacy-aware entrepreneur location visibility.



\## 5. Target Users



\### 5.1 Customers



Customers use HunarHub to discover local entrepreneurs, browse products, place orders, request services, track activities, and submit reviews.



\### 5.2 Entrepreneurs



Entrepreneurs use HunarHub to create and manage their business presence, products, services, orders, service requests, and earnings.



\### 5.3 Administrators



Administrators manage the overall platform and monitor users, entrepreneurs, categories, products, services, orders, service requests, reviews, and reports.



\## 6. Entrepreneur Categories



The platform supports the following categories:



\* Tailor

\* Potter

\* Cobbler

\* Artisan

\* Handmade Products

\* Local Vendor



\## 7. Major Modules



\### 7.1 Authentication Module



The authentication module provides:



\* User registration

\* User login

\* User logout

\* Session management

\* Current-user verification



\### 7.2 Customer Module



The customer module provides:



\* Customer dashboard

\* Marketplace browsing

\* Product search and filtering

\* Entrepreneur profiles

\* Product details

\* Product ordering

\* Order tracking

\* Service requests

\* Service-request tracking

\* Reviews and ratings

\* Profile management



\### 7.3 Entrepreneur Module



The entrepreneur module provides:



\* Entrepreneur dashboard

\* Business profile management

\* Skill and experience information

\* Availability management

\* Product management

\* Service management

\* Order management

\* Service-request management

\* Earnings information



\### 7.4 Admin Module



The admin module provides:



\* Admin dashboard

\* User management

\* Role management

\* Entrepreneur verification

\* Category management

\* Product management

\* Service management

\* Order management

\* Service-request management

\* Review management

\* Reports and statistics



\## 8. Security



HunarHub implements several security mechanisms.



\### 8.1 Password Hashing



Passwords are stored as secure Argon2 hashes instead of plain-text passwords.



\### 8.2 Authentication



Flask-Login is used for session-based user authentication.



\### 8.3 Role-Based Access Control



The system provides different permissions for:



\* CUSTOMER

\* ENTREPRENEUR

\* ADMIN



Protected routes verify the user's role before allowing access to restricted functionality.



\### 8.4 Ownership Checks



Ownership checks are used to prevent users from modifying resources that belong to another user or



