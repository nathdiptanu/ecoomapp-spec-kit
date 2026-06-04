# Product Management Requirements

## Admin Product CRUD
- Admin can view all products in a table.
- Admin can create a product with name, description, price, stock, image URL, and category.
- Admin can edit any product field.
- Admin can delete a product.

## Catalog Behavior
- Product cards show name, category, description, price, and image.
- Product detail pages show full product information and an add-to-cart control.
- Category filters and search can be used independently or together.

## Acceptance Criteria
- Seeded products appear immediately after first app start.
- Product create/update/delete changes are persisted in SQLite.
- Deleted products no longer appear in catalog results.
