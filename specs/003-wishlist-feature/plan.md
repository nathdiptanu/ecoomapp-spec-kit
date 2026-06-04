# Implementation Plan: Wishlist Feature

**Feature**: `003-wishlist-feature`

**Spec**: `specs/003-wishlist-feature/spec.md`

## Summary

Add a session-backed wishlist. Shoppers can add products to a wishlist from catalog and product detail pages, view wishlist items, remove items, and move items from wishlist to cart. Authentication is not required.

## Technical Context

- Python 3.11+
- Flask
- Flask session storage
- Flask-SQLAlchemy for product lookup
- SQLite for existing product catalog
- Jinja2 templates
- Bootstrap 5
- pytest

## Data Design

The wishlist is session-only for v1 and does not need a database table.

Session shape:

```python
session["wishlist"] = ["1", "2", "3"]
```

Rules:

- Store product IDs as strings for consistency with the existing cart session.
- Prevent duplicate product IDs.
- Remove invalid product IDs if products no longer exist.

## Route Design

- `GET /wishlist`
  - Displays wishlist items.

- `POST /wishlist/add/<product_id>`
  - Adds product to wishlist if it is not already present.
  - Redirects back to the referring page or wishlist.

- `POST /wishlist/remove/<product_id>`
  - Removes product from wishlist.
  - Redirects to wishlist.

- `POST /wishlist/move-to-cart/<product_id>`
  - Adds product to cart.
  - Removes product from wishlist.
  - Redirects to cart or wishlist.

Existing routes/templates to update:

- `GET /`
  - Catalog cards should expose add-to-wishlist action.

- `GET /products/<product_id>`
  - Product detail page should expose add-to-wishlist action.

- Base navbar
  - Add wishlist link and count.

## UI Design

Add `templates/wishlist.html`:

- Show list of saved products.
- Show remove button.
- Show move-to-cart button.
- Show empty state when no wishlist items exist.

Update:

- `templates/catalog.html`
- `templates/product_detail.html`
- `templates/base.html`

## Validation Rules

- Product must exist before adding to wishlist.
- Duplicate additions should not create repeated display rows.
- Moving a product to cart should remove it from wishlist.
- Removing the last item should show an empty wishlist state.

## Testing Strategy

Add pytest coverage for:

- Add product to wishlist from route.
- Wishlist page displays saved product.
- Duplicate add does not create duplicate entries.
- Remove wishlist item.
- Move wishlist item to cart.
- Wishlist works without authentication.

## Implementation Order

1. Add wishlist helper functions in `app/routes.py`.
2. Add wishlist count to context processor.
3. Add wishlist routes.
4. Add wishlist template.
5. Update catalog and product detail templates.
6. Add tests.
7. Run `pytest`.
8. Run the app locally and manually verify the workflow.
