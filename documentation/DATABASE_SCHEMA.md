\# HunarHub - Database Schema Documentation



\## 1. Database Information



\*\*Database Name:\*\* hunarhub



\*\*Database System:\*\* MySQL



\*\*Database Purpose:\*\* Store user accounts, entrepreneur information, marketplace products and services, orders, service requests, categories, and customer reviews.



\## 2. Database Tables



The HunarHub database contains the following main tables:



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



\## 3. Entity Relationship Overview



```text

&#x20;                   +----------------+

&#x20;                   |     users      |

&#x20;                   +----------------+

&#x20;                   | id             |

&#x20;                   | name           |

&#x20;                   | email          |

&#x20;                   | phone          |

&#x20;                   | password\_hash  |

&#x20;                   | role           |

&#x20;                   | language       |

&#x20;                   | location\_...   |

&#x20;                   +-------+--------+

&#x20;                           |

&#x20;            +--------------+--------------+

&#x20;            |                             |

&#x20;            v                             v

&#x20;  +------------------+          +------------------+

&#x20;  |  entrepreneurs   |          |     orders       |

&#x20;  +------------------+          +------------------+

&#x20;  | id               |          | id               |

&#x20;  | user\_id          |          | customer\_id      |

&#x20;  | business\_name    |          | entrepreneur\_id  |

&#x20;  | bio              |          | total\_amount     |

&#x20;  | skills           |          | status           |

&#x20;  | experience       |          +--------+---------+

&#x20;  | location         |                   |

&#x20;  | verification     |                   v

&#x20;  +--------+---------+          +------------------+

&#x20;           |                    |   order\_items    |

&#x20;           |                    +------------------+

&#x20;           |                    | order\_id         |

&#x20;           v                    | product\_id       |

&#x20;  +------------------+          | quantity         |

&#x20;  |    products      |          | unit\_price       |

&#x20;  +------------------+          +------------------+

&#x20;  | id               |

&#x20;  | entrepreneur\_id  |

&#x20;  | category\_id      |

&#x20;  | name             |

&#x20;  | description      |

&#x20;  | price            |

&#x20;  | stock            |

&#x20;  | image\_url        |

&#x20;  | status           |

&#x20;  +--------+---------+

&#x20;           |

&#x20;           v

&#x20;  +------------------+

&#x20;  |    categories    |

&#x20;  +------------------+

&#x20;  | id               |

&#x20;  | name             |

&#x20;  | description      |

&#x20;  | status           |

&#x20;  +------------------+



&#x20;  +------------------+

&#x20;  |     services     |

&#x20;  +------------------+

&#x20;  | id               |

&#x20;  | entrepreneur\_id  |

&#x20;  | category\_id      |

&#x20;  | name             |

&#x20;  | description      |

&#x20;  | price            |

&#x20;  | estimated\_time   |

&#x20;  | availability     |

&#x20;  | status           |

&#x20;  +------------------+



&#x20;  +------------------------+

&#x20;  |   service\_requests     |

&#x20;  +------------------------+

&#x20;  | id                     |

&#x20;  | customer\_id            |

&#x20;  | entrepreneur\_id        |

&#x20;  | service\_id             |

&#x20;  | request\_description    |

&#x20;  | preferred\_date         |

&#x20;  | status                 |

&#x20;  +------------------------+



&#x20;  +------------------+

&#x20;  |     reviews      |

&#x20;  +------------------+

&#x20;  | id               |

&#x20;  | customer\_id      |

&#x20;  | entrepreneur\_id  |

&#x20;  | product\_id       |

&#x20;  | rating           |

&#x20;  | review\_text      |

&#x20;  | created\_at       |

&#x20;  +------------------+

```



\## 4. Users Table



The `users` table stores account information for customers, entrepreneurs, and administrators.



\### Columns



| Column              | Type         | Description                      |

| ------------------- | ------------ | -------------------------------- |

| id                  | INT          | Primary key                      |

| name                | VARCHAR(100) | User name                        |

| email               | VARCHAR(150) | User email address               |

| phone               | VARCHAR(20)  | User phone number                |

| password\_hash       | VARCHAR(255) | Securely hashed password         |

| role                | ENUM         | CUSTOMER, ENTREPRENEUR, or ADMIN |

| language            | VARCHAR(50)  | Preferred language               |

| location\_permission | TINYINT(1)   | Location permission status       |

| created\_at          | TIMESTAMP    | Account creation time            |

| updated\_at          | TIMESTAMP    | Last update time                 |



\### Role Values



```text

CUSTOMER

ENTREPRENEUR

ADMIN

```



\## 5. Categories Table



The `categories` table stores the categories used to organize local products and services.



\### Columns



| Column      | Type    | Description          |

| ----------- | ------- | -------------------- |

| id          | INT     | Primary key          |

| name        | VARCHAR | Category name        |

| description | TEXT    | Category description |

| status      | ENUM    | ACTIVE or INACTIVE   |



\### Current Categories



```text

1\. Tailor

2\. Potter

3\. Cobbler

4\. Artisan

5\. Handmade Products

6\. Local Vendor

```



An additional category can be maintained by administrators when required.



\## 6. Entrepreneurs Table



The `entrepreneurs` table stores business information associated with entrepreneur accounts.



\### Columns



| Column              | Type       | Description               |

| ------------------- | ---------- | ------------------------- |

| id                  | INT        | Primary key               |

| user\_id             | INT        | Associated user           |

| business\_name       | VARCHAR    | Business name             |

| bio                 | TEXT       | Business introduction     |

| skill\_description   | TEXT       | Skills and services       |

| experience          | VARCHAR    | Experience information    |

| address\_area        | VARCHAR    | General business area     |

| latitude            | DECIMAL    | Latitude information      |

| longitude           | DECIMAL    | Longitude information     |

| location\_visibility | ENUM       | Location visibility level |

| verification\_status | ENUM       | Verification status       |

| availability\_status | TINYINT(1) | Entrepreneur availability |

| created\_at          | TIMESTAMP  | Record creation time      |



\### Location Visibility



```text

EXACT

AREA\_ONLY

HIDDEN

```



\### Verification Status



```text

PENDING

VERIFIED

REJECTED

```



\## 7. Products Table



The `products` table stores products listed by entrepreneurs.



\### Columns



| Column          | Type         | Description            |

| --------------- | ------------ | ---------------------- |

| id              | INT          | Primary key            |

| entrepreneur\_id | INT          | Product owner          |

| category\_id     | INT          | Product category       |

| name            | VARCHAR(150) | Product name           |

| description     | TEXT         | Product description    |

| price           | DECIMAL      | Product price          |

| stock           | INT          | Available quantity     |

| image\_url       | VARCHAR      | Product image location |

| status          | ENUM         | Product status         |

| created\_at      | TIMESTAMP    | Creation time          |

| updated\_at      | TIMESTAMP    | Last update time       |



\### Product Status



```text

ACTIVE

INACTIVE

OUT\_OF\_STOCK

```



\## 8. Services Table



The `services` table stores services offered by entrepreneurs.



\### Columns



| Column          | Type    | Description               |

| --------------- | ------- | ------------------------- |

| id              | INT     | Primary key               |

| entrepreneur\_id | INT     | Service provider          |

| category\_id     | INT     | Service category          |

| name            | VARCHAR | Service name              |

| description     | TEXT    | Service description       |

| price           | DECIMAL | Service price             |

| estimated\_time  | VARCHAR | Estimated completion time |

| availability    | VARCHAR | Service availability      |

| status          | ENUM    | ACTIVE or INACTIVE        |



\## 9. Orders Table



The `orders` table stores customer product orders.



\### Columns



| Column          | Type      | Description                      |

| --------------- | --------- | -------------------------------- |

| id              | INT       | Primary key                      |

| customer\_id     | INT       | Customer who placed the order    |

| entrepreneur\_id | INT       | Entrepreneur receiving the order |

| total\_amount    | DECIMAL   | Total order value                |

| status          | ENUM      | Order status                     |

| created\_at      | TIMESTAMP | Order creation time              |

| updated\_at      | TIMESTAMP | Last update time                 |



\### Order Status



```text

PENDING

CONFIRMED

COMPLETED

CANCELLED

```



\## 10. Order Items Table



The `order\_items` table stores the individual products included in an order.



\### Columns



| Column     | Type    | Description      |

| ---------- | ------- | ---------------- |

| id         | INT     | Primary key      |

| order\_id   | INT     | Related order    |

| product\_id | INT     | Ordered product  |

| quantity   | INT     | Ordered quantity |

| unit\_price | DECIMAL | Price per unit   |



The `order\_items` table allows one order to contain one or more products.



\## 11. Service Requests Table



The `service\_requests` table stores customer requests for entrepreneur services.



\### Columns



| Column              | Type      | Description                        |

| ------------------- | --------- | ---------------------------------- |

| id                  | INT       | Primary key                        |

| customer\_id         | INT       | Customer requesting the service    |

| entrepreneur\_id     | INT       | Entrepreneur providing the service |

| service\_id          | INT       | Requested service                  |

| request\_description | TEXT      | Customer's request details         |

| preferred\_date      | DATE      | Preferred service date             |

| status              | ENUM      | Request status                     |

| created\_at          | TIMESTAMP | Request creation time              |

| updated\_at          | TIMESTAMP | Last update time                   |



\### Service Request Status



```text

PENDING

ACCEPTED

REJECTED

COMPLETED

CANCELLED

```



\## 12. Reviews Table



The `reviews` table stores customer feedback.



\### Columns



| Column          | Type      | Description                    |

| --------------- | --------- | ------------------------------ |

| id              | INT       | Primary key                    |

| customer\_id     | INT       | Customer submitting the review |

| entrepreneur\_id | INT       | Reviewed entrepreneur          |

| product\_id      | INT       | Related product                |

| rating          | INT       | Customer rating                |

| review\_text     | TEXT      | Review content                 |

| created\_at      | TIMESTAMP | Review creation time           |



The `product\_id` field can be nullable when a review is associated with an entrepreneur or service interaction rather than a specific product.



\## 13. Main Relationships



\### User and Entrepreneur



```text

users.id

&#x20;   |

&#x20;   | 1 : 1

&#x20;   v

entrepreneurs.user\_id

```



A user account can have an associated entrepreneur profile.



\### Entrepreneur and Products



```text

entrepreneurs.id

&#x20;   |

&#x20;   | 1 : M

```

