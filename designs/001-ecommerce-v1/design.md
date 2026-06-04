# Design: E-Commerce V1

## Application Architecture
- Flask app factory in `app/__init__.py`.
- SQLAlchemy models in `app/models.py`.
- Routes in `app/routes.py`.
- Seed data in `app/seed.py`.
- Jinja2 templates in `templates/`.
- Bootstrap 5 and small custom CSS in `static/styles.css`.

## Database Design

### Category
- `id`: integer primary key
- `name`: unique category name
- `description`: short category description

### Product
- `id`: integer primary key
- `name`: product name
- `description`: product description
- `price`: numeric price
- `image_url`: remote or local image URL
- `stock`: available stock count
- `category_id`: foreign key to category

### Order
- `id`: integer primary key
- `customer_name`, `email`, `address`, `city`
- `payment_status`: defaults to simulated success
- `created_at`: order timestamp

### OrderItem
- `id`: integer primary key
- `order_id`: foreign key to order
- `product_id`: foreign key to product
- `quantity`
- `unit_price`: price snapshot at checkout

## Route Design
- `GET /`: catalog with optional `q` and `category` query parameters
- `GET /products/<id>`: product detail
- `GET /cart`: cart summary
- `POST /cart/add/<id>`: add to cart
- `POST /cart/update/<id>`: update quantity
- `POST /cart/remove/<id>`: remove item
- `GET|POST /checkout`: checkout and order creation
- `GET /orders/<id>/success`: order confirmation
- `GET /admin`: admin dashboard
- `GET /admin/products`: admin product list
- `GET|POST /admin/products/new`: create product
- `GET|POST /admin/products/<id>/edit`: update product
- `POST /admin/products/<id>/delete`: delete product
- `GET /admin/orders`: order list
- `GET /admin/orders/<id>`: order detail

## UI Design
- Responsive navbar with catalog, admin, search, and cart count.
- Catalog uses Bootstrap card grid.
- Cart and admin management use responsive tables.
- Checkout uses a two-column desktop layout and stacked mobile layout.
