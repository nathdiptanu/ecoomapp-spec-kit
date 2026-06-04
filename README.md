# SpecShop: Spec-Kit Driven Flask E-Commerce Demo

SpecShop is a sample Amazon-like e-commerce application built to demonstrate a complete Spec-Kit style workflow without Jira:

`Requirements -> Specification -> Design -> Plan -> Implementation -> Testing`

The app uses Python 3.11+, Flask, SQLAlchemy, SQLite, Jinja2 templates, Bootstrap 5, and pytest.

## What Is Included

- Product catalog with search and category filtering.
- Product detail pages.
- Session-backed shopping cart.
- Checkout form with simulated payment success.
- SQLite order persistence.
- Automatic seed data with 56 products across 8 categories.
- Simple unauthenticated admin dashboard.
- Admin product create, update, delete.
- Admin order list and order detail views.
- Local requirements, specs, designs, plans, and implementation notes.

## Repository Structure

```text
requirements/              Local Jira-style requirement documents
specs/                     Generated-style feature specifications
designs/                   Architecture, database, API, and UI design notes
plans/                     Implementation plans and task breakdowns
implementation/            Build notes
app/                       Flask application package
templates/                 Jinja2 templates
static/                    CSS assets
tests/                     pytest tests
run.py                     Local development entrypoint
requirements.txt           Python dependencies
```

## Prerequisites

- Python 3.11.1 or newer.
- Git.
- Optional for Spec-Kit learning: `uv` or `pipx`.

## Run Locally

Create and activate a virtual environment:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Start the Flask app:

```powershell
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

The SQLite database is created automatically at:

```text
instance/ecommerce.sqlite
```

Seed data is loaded automatically on first startup.

## Test

```powershell
pytest
```

The tests use an in-memory SQLite database and cover seeded data, catalog search, cart operations, checkout order creation, and admin pages.

## Spec-Kit Setup

Spec-Kit is maintained from the official GitHub repository:

[github/spec-kit](https://github.com/github/spec-kit)

The official documentation says to install from GitHub, not similarly named PyPI packages.

Persistent install with `uv`:

```powershell
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z
specify version
```

One-time use without persistent install:

```powershell
uvx --from git+https://github.com/github/spec-kit.git specify init . --script ps --integration copilot
```

Useful checks:

```powershell
specify version
specify self check
specify integration list
```

On Windows, PowerShell scripts are supported. Use `--script ps` when you want to be explicit.

## How To Use Spec-Kit For This Project

1. Initialize Spec-Kit in the repository.

```powershell
uvx --from git+https://github.com/github/spec-kit.git specify init . --script ps --integration copilot
```

2. Define project principles.

```text
/speckit.constitution Create principles for a local learning ecommerce app: keep features simple, prefer readable Flask code, use SQLite for local persistence, write tests for key workflows, avoid real payment handling in v1, and keep requirements in repository markdown files.
```

3. Write local requirements in `requirements/`.

Start with:

- `requirements/ecommerce_v1.md`
- `requirements/product_management.md`
- `requirements/checkout_flow.md`
- `requirements/future_features.md`

4. Generate the specification.

```text
/speckit.specify Build a sample Amazon-like e-commerce application for learning Spec-Kit. It should include product catalog browsing, search, category filtering, product details, shopping cart, simulated checkout, SQLite order persistence, seed data with at least 50 products, and a simple unauthenticated admin dashboard for product CRUD and order viewing. Real payments and authentication are out of scope for v1.
```

5. Clarify and validate.

```text
/speckit.clarify Focus on checkout behavior, admin product management, and seed data expectations.
/speckit.checklist
```

6. Generate the technical plan.

```text
/speckit.plan Use Python 3.11.1, Flask, Flask-SQLAlchemy, SQLite, Jinja2 templates, Bootstrap 5, app factory pattern, session-backed cart, and pytest. Keep authentication and real payments out of scope.
```

7. Generate tasks.

```text
/speckit.tasks
```

8. Analyze consistency before coding.

```text
/speckit.analyze
```

9. Implement.

```text
/speckit.implement
```

This repository already contains sample outputs for those phases under `requirements/`, `specs/`, `designs/`, `plans/`, and `implementation/`.

## Application Walkthrough

- Browse all products at `/`.
- Search with the navbar search field.
- Filter with the category dropdown.
- Open a product detail page and add the product to cart.
- Update or remove cart items at `/cart`.
- Checkout at `/checkout`.
- Click Buy Now to simulate payment success and create an order.
- View admin dashboard at `/admin`.
- Manage products at `/admin/products`.
- View orders at `/admin/orders`.

## Future Roadmap

- Add shopper accounts.
- Add admin login and roles.
- Add pagination and sort controls.
- Add product image upload support.
- Add inventory decrementing.
- Add coupons, taxes, and shipping estimates.
- Add email confirmation.
- Add real payment gateway integration.
- Add product reviews and ratings.

## Source Notes

Spec-Kit command names and installation guidance were checked against the official GitHub Spec-Kit documentation and repository on 2026-06-04.
