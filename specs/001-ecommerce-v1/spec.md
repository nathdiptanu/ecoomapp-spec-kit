# Specification: E-Commerce V1

## Functional Requirements
- FR-001: Display a searchable and filterable product catalog.
- FR-002: Provide product detail pages.
- FR-003: Support add, update, remove, and summarize cart operations.
- FR-004: Provide checkout with customer information capture.
- FR-005: Simulate payment success and persist orders in SQLite.
- FR-006: Provide unauthenticated admin product CRUD.
- FR-007: Provide admin order list and order detail views.
- FR-008: Seed at least 50 products across Electronics, Mobile Phones, Laptops, Fashion, Home & Kitchen, Books, Sports, and Toys.

## Non-Functional Requirements
- NFR-001: The application must run locally on Python 3.11+.
- NFR-002: The UI must be responsive using Bootstrap 5.
- NFR-003: SQLite is used for local persistence.
- NFR-004: The first run must not require manual data entry before browsing products.
- NFR-005: Tests must cover catalog availability, cart behavior, checkout persistence, and admin availability.

## Acceptance Criteria
- AC-001: Running the app creates the SQLite database and seed data automatically.
- AC-002: A user can search for "iPhone 15" and find the seeded product.
- AC-003: A user can add a product to cart, update quantity, and remove it.
- AC-004: A user can checkout and receive an order confirmation page.
- AC-005: Admin can view the order created by checkout.
- AC-006: Admin can create, edit, and delete products.

## Spec-Kit Prompt Example
```text
/speckit.specify Build a sample Amazon-like e-commerce application for learning Spec-Kit. It should include product catalog browsing, search, category filtering, product details, shopping cart, simulated checkout, SQLite order persistence, seed data with at least 50 products, and a simple unauthenticated admin dashboard for product CRUD and order viewing. Real payments and authentication are out of scope for v1.
```
